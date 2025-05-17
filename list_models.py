import os
import google.generativeai as genai

# Set your API key here or make sure GOOGLE_API_KEY env variable is set
<<<<<<< HEAD
genai.configure(api_key=os.getenv(""))
=======
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
>>>>>>> 4f72c51 (Removed hardcoded API keys from list_models.py and run_neovita.bat)

models = genai.list_models()
print("Available models and their supported generation methods:")
for model in models:
    print(f"- {model.name} (supports: {model.supported_generation_methods})")
