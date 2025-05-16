from google.cloud import vision
import io

def analyze_image(image):
    # Convert PIL Image to bytes
    image_byte_array = io.BytesIO()
    image.save(image_byte_array, format='PNG')
    content = image_byte_array.getvalue()

    # Initialize Google Cloud Vision API client
    client = vision.ImageAnnotatorClient()

    # Prepare the image for the API
    vision_image = vision.Image(content=content)

    # Call label detection
    response = client.label_detection(image=vision_image)

    if response.error.message:
        return f"API Error: {response.error.message}"

    labels = response.label_annotations
    found_labels = [label.description.lower() for label in labels]

    # List of health-related keywords (you can expand this list)
    illness_keywords = [
        "itch", "rash", "infection", "eczema", "redness",
        "wound", "inflammation", "skin", "irritation", "bruise"
    ]

    for keyword in illness_keywords:
        if keyword in found_labels:
            return f"⚠️ Possible sign of: {keyword.capitalize()} (AI detected)"

    return "✅ No obvious signs of distress detected in the image."
