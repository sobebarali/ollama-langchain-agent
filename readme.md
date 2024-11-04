# Reddit Restaurant Recommender

This project is a Reddit-based restaurant recommender system that uses AI to provide personalized restaurant suggestions based on user queries.

## Features

- Search across Reddit for restaurant recommendations
- Natural language processing of search results
- Intelligent filtering of comments based on upvotes
- Structured response format with restaurant details

## Setup

1. Clone the repository:
```bash
git clone https://github.com/sobebarali/reddit-restaurant-bot.git
cd reddit-restaurant-bot
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Set up environment variables:
   - Copy `.env.example` to `.env`
   - Fill in your Reddit API credentials
   - Configure Ollama settings if needed

## Usage

Basic usage example:
```python
from src.main import get_restaurant_recommendation

recommendation = get_restaurant_recommendation("best pizza in Rome")
print(recommendation)
```

## Contributing

1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Create a new Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Step 1: Project Setup

## Project Structure

```
reddit_restaurant_recommender/
├── README.md
├── requirements.txt
├── .gitignore
├── src/
│   ├── __init__.py
│   ├── main.py
│   ├── config.py
│   ├── models/
│   │   ├── __init__.py
│   │   └── data_models.py
│   ├── tools/
│   │   ├── __init__.py
│   │   └── search.py
│   ├── agents/
│   │   ├── __init__.py
│   │   └── oracle.py
│   └── utils/
│       ├── __init__.py
│       └── helpers.py
└── tests/
    ├── __init__.py
    └── test_main.py
```

In this step, we set up the basic project structure. This organization helps maintain a clean and modular codebase, making it easier to develop, test, and maintain the project.

1. Created the folder structure to separate different components of the project.
2. Added `__init__.py` files to make each folder a Python package.
3. Created `requirements.txt` for managing dependencies.
4. Added `.gitignore` to exclude unnecessary files from version control.
5. Started this README to document the project and its development process.

Why this step is important:
- Proper project structure improves code organization and readability.
- Separating concerns into different modules makes the code more maintainable.
- Setting up version control and dependency management from the start ensures a smooth development process.

Next steps will involve implementing the core functionality in each module.

## Step 2: Configuration and Data Models

In this step, we created the configuration file and defined our data models.

1. Created `src/config.py` to store configuration variables.
2. Created `src/models/data_models.py` to define Pydantic models for our data structures.

Why this step is important:
- Centralizing configuration in `config.py` makes it easy to manage and update settings.
- Using environment variables for sensitive information (like API keys) improves security.
- Defining data models with Pydantic ensures type safety and provides automatic validation.
- Clear data structures make the code more readable and maintainable.

The `Restaurant` model represents the structure of restaurant data we'll be working with. The `SearchQuery` model defines the structure of user queries, and the `SearchResult` model combines the query with a list of matching restaurants.

Next steps will involve implementing the Reddit search functionality and the AI-powered recommendation system.

## Step 3: Implement Reddit Search

In this step, we implemented the Reddit search functionality to fetch restaurant-related posts based on user queries.

1. Created `src/tools/search.py` to implement the Reddit search functionality.
2. Updated `src/main.py` to use the search tool.

Why this step is important:
- Integrating with Reddit API allows us to access a vast amount of user-generated content about restaurants.
- The search functionality forms the core of our data collection process, providing raw material for our recommendation system.
- Structuring the search results using our `Restaurant` model ensures consistency in our data handling.

The `search_reddit` function in `search.py` takes a `SearchQuery` object and returns a list of `Restaurant` objects. It uses the PRAW library to interact with Reddit's API, searching for posts in the specified subreddit that match the given query.

The `main.py` file now demonstrates basic usage of this search functionality, allowing us to test and verify that we're successfully fetching and parsing Reddit posts.

Next steps will involve implementing the AI-powered recommendation system to process and refine these search results.

## Step 4: Implement AI Recommendation System

In this step, we implemented an AI-powered recommendation system using the Ollama model to process and refine our search results.

1. Created `src/agents/oracle.py` to implement the AI recommendation system.
2. Updated `src/main.py` to use the new AI agent.

Why this step is important:
- The AI system enhances raw Reddit data, providing more structured and refined recommendations.
- It allows for filling in missing details and standardizing the restaurant information.
- The use of LangChain and Ollama demonstrates integration of advanced AI capabilities into our application.

The `get_ai_recommendations` function in `oracle.py` takes the original search query and Reddit results, processes them using an Ollama model, and returns refined `Restaurant` objects with enhanced information.

Next steps will involve error handling, testing, and potentially adding a user interface for easier interaction with the system.