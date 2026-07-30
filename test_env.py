import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Try to get the API key
api_key = os.getenv("GEMINI_API_KEY")

if api_key:
    print(f"Key found in .env: {api_key}")
else:
    print("Error: GEMINI_API_KEY not found in .env via test_env.py")

print("--- RAW .env content attempt ---")
try:
    with open('.env', 'r', encoding='utf-8') as f:
        content = f.read()
        print(f"Content of .env file:\n---\n{content}\n---")
except Exception as e:
    print(f"Could not read .env file content: {e}")