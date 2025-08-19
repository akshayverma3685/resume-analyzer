import streamlit as st
from resume_parser import extract_text_from_pdf, extract_text_from_docx
from analyzer import analyze_resume

st.set_page_config(page_title="AI Resume Analyzer", layout="wide")

st.title("📄 AI-Powered Resume Analyzer")
st.write("Upload your resume (PDF/DOCX) and get an ATS score + skill analysis.")

uploaded_file = st.file_uploader("Upload Resume", type=["pdf", "docx"])

if uploaded_file:
    # Extract text
    if uploaded_file.type == "application/pdf":
        text = extract_text_from_pdf(uploaded_file)
    else:
        text = extract_text_from_docx(uploaded_file)

    if text.strip() == "":
        st.error("❌ Could not extract text. Please try another file.")
    else:
        # Analyze
        results = analyze_resume(text)

        st.subheader("✅ Resume Analysis Results")
        st.write(f"**ATS Score:** {results['score']} / 100")

        st.success("Skills Found: " + ", ".join(results['found']) if results['found'] else "No skills found")
        st.warning("Missing Skills: " + ", ".join(results['missing']) if results['missing'] else "None 🎉")

        st.text_area("📄 Extracted Resume Text", text, height=200)
