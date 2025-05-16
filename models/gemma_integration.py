import os
import google.generativeai as genai

# Configure Gemini API key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Initialize the Gemini Pro model
model = genai.GenerativeModel("gemini-1.5-pro")

def analyze_symptoms(text: str) -> str:
    """Generate a response analyzing symptoms using Gemini."""
    try:
        response = model.generate_content(text)
        return response.text
    except Exception as e:
        return f"Error analyzing symptoms: {e}"
