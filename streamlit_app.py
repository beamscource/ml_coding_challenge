import streamlit as st
import requests
from requests_toolbelt.multipart.encoder import MultipartEncoder
from PIL import Image

st.title("Codepan Coding Challenge: Predicting Feet Fashion")

st.text("Quite often people might leave their homes in sandals during deep winter.")
col1, col2, col3 = st.columns(3)
col2.image('assets/snow.jpg', use_column_width=True)
st.text("To prevent this from happening, we trained a feed-forward neural network \nto\
support you in choosing the right attire for the right occasion.")

uploaded_file = st.file_uploader(
    "Please select an image to classify the shoe type", type=["jpg", "jpeg"], 
    accept_multiple_files=False
)

if uploaded_file:
    original_image = Image.open(uploaded_file).convert("RGB")
    col1, col2, col3 = st.columns(3)
    col2.header("This looks to me like a...")
    col2.image(original_image)
    m = MultipartEncoder(fields={"file": ("filename", uploaded_file, "image/jpeg")})
    req = requests.post(
        "http://localhost:8000/score", data=m,
        headers={"Content-Type": m.content_type}, timeout=8000
    )
    col2.header(max(req.json(), key=req.json().get).lower() + '!')
    st.text("Got response from backend API:")
    st.text(req.json())
