from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages import AIMessage
from langchain_core.output_parsers import JsonOutputParser
from langchain_ollama.llms import OllamaLLM
from config import OLLAMA_MODEL, SEARCH_LIMIT
from models.data_models import Restaurant, SearchQuery, SearchResult
import json
import logging

# Setup basic logging
logging.basicConfig(level=logging.INFO)

def extract_json_from_string(s: str) -> dict:
    """
    Extract and return the JSON object from a string.
    It looks for the first JSON-like structure in the string and tries to parse it.

    Args:
        s (str): The string to extract JSON from.

    Returns:
        dict: Parsed JSON object.

    Raises:
        ValueError: If no valid JSON is found or if JSON is malformed.
    """
    json_start = s.find('{')
    json_end = s.rfind('}')
    if json_start != -1 and json_end != -1:
        try:
            return json.loads(s[json_start:json_end+1])
        except json.JSONDecodeError as e:
            raise ValueError("Invalid JSON structure") from e
    raise ValueError("No JSON found in the string")


def get_ai_recommendations(query: SearchQuery, reddit_results: list[Restaurant]) -> SearchResult:
    """
    Process the search results using AI to get refined recommendations.
    
    Args:
        query (SearchQuery): The original search query.
        reddit_results (list[Restaurant]): List of Restaurant objects from Reddit results.
    
    Returns:
        SearchResult: Refined search result with AI recommendations.
    """
    
    model = OllamaLLM(model=OLLAMA_MODEL)
    
    prompt = ChatPromptTemplate.from_template(
        """
        You are an AI assistant specializing in restaurant recommendations. 
        Given the following search query and list of restaurants, provide the top {search_limit} recommendations.
        Enhance the restaurant information where possible, filling in missing details.

        Search Query: {query}

        Restaurants:
        {restaurants}

        Provide your recommendations in the following JSON format:
        {{
            "recommendations": [
                {{
                    "name": "Restaurant Name",
                    "description": "Brief description",
                    "cuisine": "Cuisine type",
                    "price_range": "$ or $$ or $$$ or $$$$",
                    "location": "Location",
                    "rating": 4.5
                }}
            ]
        }}
        """
    )
    
    chain = prompt | model
    
    # Convert Restaurant objects to strings
    restaurant_strings = [
        f"{r.name}: {r.description}. Cuisine: {r.cuisine}, Price: {r.price_range}, Location: {r.location}, Rating: {r.rating}"
        for r in reddit_results
    ]
    
    input_data = {
        "query": query.query,
        "location": query.location,
        "restaurants": "\n".join(restaurant_strings),
        "search_limit": SEARCH_LIMIT
    }
    
    logging.info(f"Invoking model with query: {query.query} and {len(reddit_results)} restaurants.")
    
    try:
        # Run the model and get the raw result
        result = chain.invoke(input_data)
        logging.info("Model returned raw result.")
    except Exception as e:
        logging.error(f"Error invoking the AI model: {e}")
        return SearchResult(query=query, restaurants=[])
    
    # Parse the model's output
    output_parser = JsonOutputParser()
    
    try:
        message = AIMessage(content=result)
        parsed_result = output_parser.invoke(message)
    except Exception as e:
        logging.warning(f"Failed to parse AI output using JsonOutputParser: {e}")
        # Fallback to manual JSON extraction
        try:
            parsed_result = extract_json_from_string(result)
        except ValueError as ve:
            logging.error(f"Error extracting JSON: {ve}")
            return SearchResult(query=query, restaurants=[])
    
    # Return structured SearchResult
    try:
        return SearchResult(
            query=query,
            restaurants=[
                Restaurant(**restaurant)
                for restaurant in parsed_result.get("recommendations", [])
            ]
        )
    except (KeyError, TypeError) as e:
        logging.error(f"Error processing final result: {e}")
        return SearchResult(query=query, restaurants=[])
