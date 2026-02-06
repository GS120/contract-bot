import streamlit as st
import PyPDF2
import docx

# -----------------------------
# Function to extract text from uploaded file
# -----------------------------
def extract_text(file):
    # TXT file
    if file.name.endswith(".txt"):
        return file.read().decode("utf-8")

    # PDF file
    elif file.name.endswith(".pdf"):
        reader = PyPDF2.PdfReader(file)
        text = ""
        for page in reader.pages:
            if page.extract_text():
                text += page.extract_text()
        return text

    # DOCX file
    elif file.name.endswith(".docx"):
        document = docx.Document(file)
        text = ""
        for para in document.paragraphs:
            text += para.text + "\n"
        return text

    return ""


# -----------------------------
# Streamlit App UI
# -----------------------------
st.title("📑 Contract Analysis & Risk Bot")
st.write("Upload a contract file and get risk analysis instantly.")

uploaded_file = st.file_uploader(
    "Upload a contract file",
    type=["txt", "pdf", "docx"]
)

# -----------------------------
# Main Logic
# -----------------------------
if uploaded_file:
    st.success("✅ File uploaded successfully!")

    # Extract content
    content = extract_text(uploaded_file)

    # Show contract text
    st.subheader("📄 Contract Content")
    st.text_area("Contract Text", content, height=250)

    # Risk keywords
    issues = []
    recommendations = []
    score = 0

    # Clause Detection
    if "penalty" in content.lower():
        issues.append("⚠️ Penalty clause found")
        recommendations.append("✔ Review penalty terms carefully.")
