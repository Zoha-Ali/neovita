from google.cloud import vision
from google.oauth2 import service_account
import io
import streamlit as st

def analyze_image(image) -> str:
    """Analyze the image with Google Cloud Vision API and return labels."""

    # Load credentials from Streamlit secrets
    credentials_dict = st.secrets["google_cloud"]
    credentials = service_account.Credentials.from_service_account_info(credentials_dict)

    # Use credentials in the Vision client
    client = vision.ImageAnnotatorClient(credentials=credentials)

    # Convert PIL image to bytes
    img_byte_arr = io.BytesIO()
    image.save(img_byte_arr, format=image.format)
    content = img_byte_arr.getvalue()

    vision_image = vision.Image(content=content)
    response = client.label_detection(image=vision_image)

    if response.error.message:
        raise Exception(f"Vision API error: {response.error.message}")

    labels = response.label_annotations
    results = [label.description for label in labels]

    return ", ".join(results)
