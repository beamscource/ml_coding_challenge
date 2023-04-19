import streamlit as st
import requests
from requests_toolbelt.multipart.encoder import MultipartEncoder

st.title("Codepan Coding Challenge")

st.text("Hello World!")

uploaded_file = st.file_uploader(
    "Please select file to upload", type=["jpg", "jpeg"], accept_multiple_files=False
)

if uploaded_file:
    m = MultipartEncoder(fields={"file": ("filename", uploaded_file, "image/jpeg")})
    st.text("Got response from backend API:")
    req = requests.post(
        "http://localhost:8000/score", data=m, headers={"Content-Type": m.content_type}, timeout=8000
    )
    st.text(req.json())
