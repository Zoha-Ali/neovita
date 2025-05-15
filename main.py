
import streamlit as st
from models.gemini_integration import analyze_symptoms
from models.gemma_integration import analyze_image
from PIL import Image

st.set_page_config(page_title="Neovita - Infant Health Checker", layout="centered")

st.title("👶 Neovita: Early Illness Detection for Infants")
st.write("Upload a photo of your baby and/or describe symptoms to detect early signs of illness.")

uploaded_file = st.file_uploader("Upload baby image", type=["jpg", "jpeg", "png"])
if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded image", use_column_width=True)
    if st.button("Analyze Image"):
        with st.spinner("Analyzing image with Gemma..."):
            result = analyze_image(image)
            st.success(f"Prediction: {result}")

symptoms = st.text_area("Describe symptoms")
if symptoms and st.button("Analyze Symptoms"):
    with st.spinner("Analyzing symptoms with Gemini..."):
        response = analyze_symptoms(symptoms)
        st.success(f"Prediction: {response}")
