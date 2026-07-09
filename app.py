from pathlib import Path

import numpy as np
import streamlit as st
import tensorflow as tf
from PIL import Image

CLASS_NAMES = [
    "manmade_pothole",
    "no_pothole",
    "pothole",
]

CLASS_LABELS = {
    "manmade_pothole": "Man-made Pothole",
    "no_pothole": "No Pothole",
    "pothole": "Pothole",
}

MODEL_PATH = Path(__file__).parent / "road_damage_classifier.keras"


def preprocess(image):
    image = image.resize((224, 224))
    img = np.array(image)
    img = img / 255.0
    img = np.expand_dims(img, axis=0)
    return img


@st.cache_resource
def load_model():
    if not MODEL_PATH.exists():
        raise FileNotFoundError(
            f"Model file not found. Place `road_damage_classifier.keras` in:\n{MODEL_PATH.parent}"
        )
    return tf.keras.models.load_model(str(MODEL_PATH))


st.set_page_config(
    page_title="Road Damage Detection",
    page_icon="🛣️",
    layout="wide",
)

st.title("🛣️ Road Damage Classification")
st.caption("Upload a road image to detect potholes and road damage using AI.")

with st.sidebar:
    st.header("About")
    st.markdown(
        """
        This app classifies road images into:

        - **Man-made Pothole**
        - **No Pothole**
        - **Pothole**

        Supported formats: JPG, JPEG, PNG
        """
    )

try:
    model = load_model()
except FileNotFoundError as exc:
    st.error(str(exc))
    st.stop()
except Exception as exc:
    st.error(f"Failed to load model: {exc}")
    st.stop()

uploaded_file = st.file_uploader(
    "Upload Road Image",
    type=["jpg", "jpeg", "png"],
)

if uploaded_file is not None:
    image = Image.open(uploaded_file).convert("RGB")
    img = preprocess(image)

    with st.spinner("Analyzing image..."):
        prediction = model.predict(img, verbose=0)[0]

    confidence = float(np.max(prediction))
    class_index = int(np.argmax(prediction))
    predicted_class = CLASS_NAMES[class_index]
    predicted_label = CLASS_LABELS[predicted_class]

    col1, col2 = st.columns([1.2, 1])

    with col1:
        st.subheader("Uploaded Image")
        st.image(image, use_container_width=True)

    with col2:
        st.subheader("Prediction Result")
        st.success(f"**{predicted_label}**")
        st.metric("Confidence", f"{confidence * 100:.2f}%")

        st.markdown("**Class probabilities**")
        for name, prob in zip(CLASS_NAMES, prediction):
            st.progress(float(prob), text=f"{CLASS_LABELS[name]}: {prob * 100:.1f}%")
else:
    st.info("Upload a road image to get started.")
