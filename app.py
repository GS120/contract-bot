import streamlit as st

st.title("Contract Analysis & Risk Bot")

uploaded_file = st.file_uploader("Upload a contract file", type=["txt"])

if uploaded_file:
    st.success("File uploaded successfully!")
  content = uploaded_file.read().decode("utf-8")
    st.text_area("Contract Content", content, height=300)
