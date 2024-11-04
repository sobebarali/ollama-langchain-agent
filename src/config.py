import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Reddit API credentials
REDDIT_CLIENT_ID = os.getenv("REDDIT_CLIENT_ID")
REDDIT_CLIENT_SECRET = os.getenv("REDDIT_CLIENT_SECRET")
REDDIT_USER_AGENT = os.getenv("REDDIT_USER_AGENT")

# Subreddit to search
SUBREDDIT_NAME = "restaurants"

# Number of posts to fetch
NUM_POSTS = 100

# Ollama model name
OLLAMA_MODEL = "llama3.2"

# Search result limit
SEARCH_LIMIT = 5

