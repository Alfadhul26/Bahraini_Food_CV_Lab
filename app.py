import streamlit as st
from ultralytics import YOLO
from PIL import Image

model = YOLO("best.pt")

st.title("Bahraini Dishes Detector")

file = st.file_uploader("Upload a dish photo", type=["jpg", "jpeg", "png"])

if file:
    results = model(Image.open(file))
    st.image(results[0].plot()[..., ::-1])
