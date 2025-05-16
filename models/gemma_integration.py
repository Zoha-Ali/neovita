import google.generativeai as genai

# Use your API key here directly (or via env variable)
genai.configure(api_key="REMOVED")

model = genai.GenerativeModel("gemini-pro")

def analyze_symptoms(text):
    response = model.generate_content(text)
    return response.text
