import streamlit as st
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import load_img, img_to_array
import numpy as np

# Load the trained model
MODEL_PATH = "best_mobilenet_model.keras"
model = load_model(MODEL_PATH)

# Define class labels
class_labels = {0: "Household Waste", 1: "Recyclable"}

# Streamlit interface
st.title("Recycling Classification App")
st.write("Upload an image, and the model will classify it as either 'Recyclable' or 'Household Waste'.")

# File uploader
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Display uploaded image
    st.image(uploaded_file, caption="Uploaded Image", use_column_width=True)
    st.write("Classifying...")
    
    # Preprocess the image
    img = load_img(uploaded_file, target_size=(224, 224))
    img_array = img_to_array(img) / 255.0  # Normalize to [0, 1]
    img_array = np.expand_dims(img_array, axis=0)  # Add batch dimension
    
    # Make prediction
    prediction = model.predict(img_array)
    predicted_class = 1 if prediction > 0.5 else 0
    confidence = prediction[0][0] if predicted_class == 1 else 1 - prediction[0][0]
    
    # Display result
    st.write(f"Prediction: **{class_labels[predicted_class]}**")
    st.write(f"Confidence: **{confidence:.2f}**")
