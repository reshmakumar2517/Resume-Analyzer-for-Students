import streamlit as st
import pdfplumber
import re

st.set_page_config(page_title="Resume Analyzer")

st.title("Resume Analyzer for Students")

uploaded_file = st.file_uploader(
    "Upload Your Resume (PDF)",
    type=["pdf"]
)

if uploaded_file is not None:

    text = ""

    with pdfplumber.open(uploaded_file) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()

            if page_text:
                text += page_text

    score = 0

    st.subheader("Resume Analysis Result")

    # Email Check
    email_pattern = r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}"
    emails = re.findall(email_pattern, text)

    if emails:
        st.success("✅ Email Found")
        score += 20
    else:
        st.error("❌ Email Not Found")

    # Phone Check
    phone_pattern = r"(\+91[- ]?)?[6-9]\d{9}"
    phones = re.findall(phone_pattern, text)

    if phones:
        st.success("✅ Phone Number Found")
        score += 20
    else:
        st.error("❌ Phone Number Not Found")

    # Skills Check
    skills = [
        "python",
        "java",
        "c",
        "c++",
        "sql",
        "html",
        "css",
        "javascript"
    ]

    found_skills = []

    for skill in skills:
        if skill.lower() in text.lower():
            found_skills.append(skill)

    st.subheader("Skills Found")

    if found_skills:
        for skill in found_skills:
            st.write("✅", skill.upper())
        score += 30
    else:
        st.write("No Skills Found")

    # Project Check
    if "project" in text.lower():
        st.success("✅ Project Section Found")
        score += 30
    else:
        st.warning("⚠️ Project Section Missing")

    # ATS Score
    st.subheader("ATS Score")

    st.write(f"{score}/100")

    st.progress(score / 100)

    if score >= 80:
        st.success("Excellent Resume")
    elif score >= 60:
        st.warning("Good Resume - Add More Skills")
    else:
        st.error("Needs Improvement")

    # Suggestions
    st.subheader("Suggestions")

    if score < 100:
        st.write("• Add Certifications")
        st.write("• Add LinkedIn Profile")
        st.write("• Add More Technical Skills")
        st.write("• Add Internship Experience")