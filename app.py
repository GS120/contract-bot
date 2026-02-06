import streamlit as st
import PyPDF2
import docx

# -----------------------------
# Extract text from uploaded file
# -----------------------------
def extract_text(file):
    if file.name.endswith(".txt"):
        return file.read().decode("utf-8")

    elif file.name.endswith(".pdf"):
        reader = PyPDF2.PdfReader(file)
        text = ""
        for page in reader.pages:
            if page.extract_text():
                text += page.extract_text()
        return text

    elif file.name.endswith(".docx"):
        document = docx.Document(file)
        text = ""
        for para in document.paragraphs:
            text += para.text + "\n"
        return text

    return ""


# -----------------------------
# Simple AI-style Summary Generator
# -----------------------------
def generate_summary(text):
    lines = text.split("\n")
    clean_lines = [l.strip() for l in lines if len(l.strip()) > 20]

    summary = clean_lines[:5]  # first 5 meaningful lines
    return summary


# -----------------------------
# Streamlit App UI
# -----------------------------
st.title("📑 AI Contract Risk Assessment Bot")
st.write("Upload a contract file and get summary + risk analysis instantly.")

uploaded_file = st.file_uploader(
    "Upload Contract File",
    type=["txt", "pdf", "docx"]
)

# -----------------------------
# Main Logic
# -----------------------------
if uploaded_file:
    st.success("✅ File uploaded successfully!")

    # Extract contract content
    content = extract
