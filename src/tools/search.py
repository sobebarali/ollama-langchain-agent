import praw
from typing import List
from config import REDDIT_CLIENT_ID, REDDIT_CLIENT_SECRET, REDDIT_USER_AGENT, SUBREDDIT_NAME, NUM_POSTS
from models.data_models import Restaurant, SearchQuery

def create_reddit_instance():
    """Create and return a Reddit instance using credentials from config."""
    return praw.Reddit(
        client_id=REDDIT_CLIENT_ID,
        client_secret=REDDIT_CLIENT_SECRET,
        user_agent=REDDIT_USER_AGENT
    )

def search_reddit(query: SearchQuery) -> List[Restaurant]:
    """
    Search Reddit for restaurant recommendations based on the given query.
    
    Args:
        query (SearchQuery): The search query containing user preferences.
    
    Returns:
        List[Restaurant]: A list of Restaurant objects based on Reddit posts.
    """
    reddit = create_reddit_instance()
    subreddit = reddit.subreddit(SUBREDDIT_NAME)
    
    # Construct search query string
    search_string = f"{query.query}"
    if query.location:
        search_string += f" {query.location}"
    if query.cuisine:
        search_string += f" {query.cuisine}"
    if query.price_range:
        search_string += f" {query.price_range}"
    
    restaurants = []
    for post in subreddit.search(search_string, limit=NUM_POSTS):
        # Basic parsing of post title to extract restaurant information
        # This is a simplistic approach and might need refinement
        restaurant = Restaurant(
            name=post.title.split(' - ')[0] if ' - ' in post.title else post.title,
            description=post.selftext[:200] + '...' if len(post.selftext) > 200 else post.selftext
        )
        restaurants.append(restaurant)
    
    return restaurants
