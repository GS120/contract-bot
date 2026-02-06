import streamlit as st

# Title
st.title("Contract Analysis & Risk Bot")

# Upload File
uploaded_file = st.file_uploader(
    "Upload a contract file",
    type=["txt", "pdf", "docx"]
)

if uploaded_file:

    st.success("File uploaded successfully!")

    # Read TXT File
    if uploaded_file.name.endswith(".txt"):
        content = uploaded_file.read().decode("utf-8")

    # PDF File Placeholder
    elif uploaded_file.name.endswith(".pdf"):
        content = "PDF support will be added soon."

    # DOCX File Placeholder
    elif uploaded_file.name.endswith(".docx"):
        content = "DOCX support will be added soon."

    # Display Contract Content
    st.subheader("Contract Content")
    st.text_area("Text inside contract:", content, height=300)

    # Risk Detection
    st.subheader("Contract Risk Analysis")

    risk_score = 0

    if "penalty" in content.lower():
        st.warning("⚠️ Penalty clause found")
        risk_score += 3

    if "liable" in content.lower() or "liability" in content.lower():
        st.warning("⚠️ Liability limitation found")
        risk_score += 2

    if "terminate" in content.lower():
        st.warning("⚠️ Termination clause found")
        risk_score += 2

    # Final Risk Result
    st.subheader("Final Risk Level")

    if risk_score >= 6:
        st.error("🔴 HIGH RISK Contract")
    elif risk_score >= 3:
        st.warning("🟠 MEDIUM RISK Contract")
    else:
        st.success("🟢 LOW RISK Contract")

    st.write("Risk Score =", risk_score)
# -----------------------------
# Download Report Button
# -----------------------------
report_text = f"""
Contract Risk Report
---------------------

Risk Score: {score}
Risk Level: {level}

Issues Found:
{chr(10).join(issues)}

Recommendations:
{chr(10).join(recommendations)}
"""

st.download_button(
    label="📥 Download Risk Report",
    data=report_text,
    file_name="contract_risk_report.txt",
    mime="text/plain"
)
