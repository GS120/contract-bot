import streamlit as st

# Title
st.title("Contract Analysis & Risk Bot")

# Upload File
uploaded_file = st.file_uploader(
    "Upload a contract file",
    type=["txt"]
)

# Function to check contract risk
def analyze_contract(text):
    risk_score = 0
    issues = []
    recommendations = []

    # Penalty Clause
    if "penalty" in text.lower():
        risk_score += 3
        issues.append("⚠️ Penalty clause found")
        recommendations.append(
            "➡️ Recommendation: Negotiate to reduce penalty amount or add fair exit terms."
        )

    # Long Commitment Clause
    if "2 years" in text.lower() or "3 years" in text.lower():
        risk_score += 2
        issues.append("⚠️ Long commitment clause found")
        recommendations.append(
            "➡️ Recommendation: Try to shorten the commitment period or include early exit options."
        )

    # Liability Clause
    if "not responsible" in text.lower() or "no liability" in text.lower():
        risk_score += 2
        issues.append("⚠️ Liability limitation found")
        recommendations.append(
            "➡️ Recommendation: Ensure both parties share responsibilities fairly."
        )

    # Final Risk Level
    if risk_score >= 6:
        level = "🔴 HIGH RISK Contract"
    elif risk_score >= 3:
        level = "🟠 MEDIUM RISK Contract"
    else:
        level = "🟢 LOW RISK Contract"

    return risk_score, level, issues, recommendations


# Main Logic
if uploaded_file:
    content = uploaded_file.read().decode("utf-8")

    st.subheader("📄 Uploaded Contract Content")
    st.text_area("Contract Text", content, height=200)

    # Analyze
    score, level, issues, recommendations = analyze_contract(content)

    st.subheader("📊 Risk Analysis Result")
    st.write("### Risk Score:", score)
    st.write("### Final Risk Level:", level)

    st.subheader("⚠️ Issues Found")
    if issues:
        for i in issues:
            st.write(i)
    else:
        st.write("✅ No risky clauses detected.")

    st.subheader("✅ Recommendations")
    if recommendations:
        for r in recommendations:
            st.write(r)
    else:
        st.write("✅ Contract looks safe. No changes needed.")
