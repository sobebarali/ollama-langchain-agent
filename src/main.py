from models.data_models import SearchQuery
from tools.search import search_reddit
from agents.oracle import get_ai_recommendations


def main():
    # Example usage
    query = SearchQuery(query="best pizza", location="New York")
    reddit_results = search_reddit(query)
    
    ai_results = get_ai_recommendations(query, reddit_results)
    
    print(f"AI Results: {ai_results}")
    
    # print(f"AI Recommendations:")
    # for restaurant in ai_results.restaurants:
    #     print(f"- {restaurant.name}")
    #     print(f"  Cuisine: {restaurant.cuisine}")
    #     print(f"  Price Range: {restaurant.price_range}")
    #     print(f"  Location: {restaurant.location}")
    #     print(f"  Rating: {restaurant.rating}")
    #     print(f"  Description: {restaurant.description[:100]}...")
    #     print()

if __name__ == "__main__":
    main()
