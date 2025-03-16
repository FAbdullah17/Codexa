import streamlit as st
import requests

# Streamlit UI Title
st.title("Code Copilot: AI-Powered Code Assistant")

# Task selection dropdown
task = st.selectbox("Choose Task:", ["Code Explanation", "Code Generation", "Code Debugging"])
user_input = st.text_area("Enter your code or prompt:")

# Process request on button click
if st.button("Submit"):
    if user_input:
        response = requests.post("http://localhost:8000/generate", json={"prompt": user_input})
        if response.status_code == 200:
            st.code(response.json()["response"], language="python")
        else:
            st.error("Error processing request.")
