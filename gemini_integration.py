
def analyze_symptoms(text):
    if "fever" in text.lower() or "rash" in text.lower():
        return "Possible viral infection. Monitor and consult a pediatrician."
    elif "cough" in text.lower():
        return "Symptoms suggest respiratory infection. Seek medical advice."
    else:
        return "Symptoms not recognized. Please consult a doctor for accurate diagnosis."
