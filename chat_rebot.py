import os

from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Access your API key
openai_api_key = os.getenv("OPENAI_API_KEY")