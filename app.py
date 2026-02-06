import streamlit as st

st.title("Contract Analysis & Risk Bot")

uploaded_file = st.file_uploader(
    "Upload a contract file",
    type=["txt", "pdf", "docx"]
)

if uploaded_file:
    st.success("File uploaded successfully!")

    # Read file content (TXT only)
    content = uploaded_file.read().decode("utf-8")

    st.subheader("Contract Content")
    st.text_area("Text", content, height=200)

    # Risk scoring
    score = 0
    risks = []

    if "penalty" in content.lower():
        score += 3
        risks.append("Penalty clause found")

    if "liability" in content.lower():
        score += 2
        risks.append("Liability limitation found")

    if "commitment" in content.lower():
        score += 2
        risks.append("Long commitment clause found")

    st.subheader("Final Risk Level")

    if score >= 6:
        st.error("HIGH RISK Contract")
    elif score >= 3:
        st.warning("MEDIUM RISK Contract")
    else:
        st.success("LOW RISK Contract")

    st.write(f"Risk Score: {score}")

    st.subheader("Risk Factors Found")
    for r in risks:
        st.write("⚠️", r)
