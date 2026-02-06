import streamlit as st

st.title("📄 Contract Analysis & Risk Bot")

uploaded_file = st.file_uploader(
    "Upload a contract file (.txt only)",
    type=["txt"]
)

if uploaded_file:
    st.success("✅ File uploaded successfully!")

    # Read contract text
    content = uploaded_file.read().decode("utf-8")

    st.subheader("📌 Contract Content")
    st.text_area("Contract Text", content, height=250)

    # Risk detection keywords
    risk_points = 0
    risks_found = []

    # Penalty Clause
    if "penalty" in content.lower() or "fine" in content.lower():
        risks_found.append("⚠️ Penalty clause found")
        risk_points += 3

    # Liability Clause
    if "not responsible" in content.lower() or "liability" in content.lower():
        risks_found.append("⚠️ Liability limitation found")
        risk_points += 2

    # Long Commitment
    if "2 years" in content.lower() or "3 years" in content.lower():
        risks_found.append("⚠️ Long commitment clause found")
        risk_points += 2

    # Final Result
    st.subheader("📊 Contract Risk Analysis")

    if risks_found:
        for r in risks_found:
            st.write(r)
    else:
        st.write("✅ No major risks detected.")

    # Risk Level
    st.subheader("✅ Final Risk Level")

    if risk_points >= 6:
        st.error("🔴 HIGH RISK Contract")
    elif risk_points >= 3:
        st.warning("🟠 MEDIUM RISK Contract")
    else:
        st.success("🟢 LOW RISK Contract")

    st.write("Risk Score =", risk_points)
