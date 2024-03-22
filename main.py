# We need to import the api key from the .env
from dotenv import load_dotenv
import os
from e2b import Sandbox

load_dotenv()

# Import the API key
API_KEY = os.getenv("E2B_API_KEY")

sandbox = Sandbox(API_KEY)
# sandbox.close()
