import os
import google.generativeai as genai

# Set API key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Create the model object
model = genai.GenerativeModel("gemini-pro")

def analyze_symptoms(text):
    response = model.generate_content(text)
    return response.text
