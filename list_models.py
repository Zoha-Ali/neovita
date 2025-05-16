import os
import google.generativeai as genai

# Set your API key here or make sure GOOGLE_API_KEY env variable is set
genai.configure(api_key=os.getenv("REMOVED"))

models = genai.list_models()
print("Available models and their supported generation methods:")
for model in models:
    print(f"- {model.name} (supports: {model.supported_generation_methods})")
