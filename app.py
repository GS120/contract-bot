import streamlit as st
import PyPDF2
import docx

st.set_page_config(page_title="Contract Risk Bot", layout="wide")

st.title("📑 Contract Analysis & Risk Bot")
st.write("Upload a contract file and get risk detection instantly.")

# ---------- File Upload ----------
uploaded_file = st.file_uploader(
    "📌 Upload Contract File",
    type=["txt", "pdf", "docx"]
)

# ---------- Extract Text Function ----------
def extract_text(file):
    if file.name.endswith(".txt"):
        return file.read().decode("utf-8")

    elif file.name.endswith(".pdf"):
        pdf_reader = PyPDF2.PdfReader(file)
        text = ""
        for page in pdf_reader.pages:
            text += page.extract_text()
        return text

    elif file.name.endswith(".docx"):
        doc = docx.Document(file)
        return "\n".join([p.text for p in doc.paragraphs])

    return ""


# ---------- Main Logic ----------
if uploaded_file:
    st.success("✅ File uploaded successfully!")

    content = extract_text(uploaded_file)

    # Show Content
    with st.expander("📄 View Contract Content"):
        st.text_area("Contract Text", content, height=250)

    # ---------- Risk Scoring ----------
    score = 0
    risks = []

    if "penalty" in content.lower():
        score += 3
        risks.append("⚠️ Penalty clause found")

    if "liability" in content.lower():
        score += 2
        risks.append("⚠️ Liability limitation found")

    if "commitment" in content.lower():
        score += 2
        risks.append("⚠️ Long-term commitment found")

    if "termination" in content.lower():
        score += 2
        risks.append("⚠️ Termination clause detected")

    # ---------- Final Risk Level ----------
    st.subheader("📌 Final Risk Result")

    if score >= 7:
        level = "HIGH RISK"
        st.error("🚨 HIGH RISK Contract")
    elif score >= 4:
        level = "MEDIUM RISK"
        st.warning("⚠️ MEDIUM RISK Contract")
    else:
        level = "LOW RISK"
        st.success("✅ LOW RISK Contract")

    st.write(f"### Risk Score: **{score}**")

    # ---------- Risk Factors ----------
    st.subheader("🔍 Risk Factors Found")

    if risks:
        for r in risks:
            st.write(r)
    else:
        st.write("✅ No major risky clauses found.")

    # ---------- Download Report ----------
    report_text = f"""
CONTRACT RISK REPORT
--------------------
Final Risk Level: {level}
Risk Score: {score}

Risk Factors Found:
{chr(10).join(risks) if risks else "No major risks detected."}
"""

    st.download_button(
        label="⬇️ Download Risk Report",
        data=report_text,
        file_name="contract_risk_report.txt",
        mime="text/plain"
    )
