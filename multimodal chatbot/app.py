# app.py

import streamlit as st
from rag import explain

st.title(" Finance AI Assistant")

uploaded_file = st.file_uploader("Upload receipt / invoice", type=["png", "jpg", "pdf"])
question = st.text_input("Ask a question")

if uploaded_file:
    with open("temp_file", "wb") as f:
        f.write(uploaded_file.read())

    if question:
        answer = explain(question, "temp_file")
        st.write("### Answer")
        st.write(answer)