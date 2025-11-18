import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

api_key = os.getenv("GOOGLE_API_KEY")
if not api_key:
    raise ValueError("❌ GOOGLE_API_KEY is missing in .env file")

# Configure Gemini
genai.configure(api_key=api_key)

print("\nFetching available Gemini models...\n")

# List all models
models = genai.list_models()

for m in models:
    print("🔹", m.name)