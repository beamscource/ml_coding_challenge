from distutils.command.upload import upload
import streamlit as st
import requests

st.title("Codepan Coding Challenge")

st.text("Hello World!")

uploaded_file = st.file_uploader(
    "Please select file to upload", type=["jpg", "jpeg"], accept_multiple_files=False
)

if uploaded_file:
    st.text("Got response from backend API:")
    req = requests.post("http://localhost:8000/score")
    st.text(req.json())
