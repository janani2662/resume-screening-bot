import streamlit as st
from src.parser import extract_text
from src.matcher import get_match_score
import tempfile

st.title("AI Resume Screening Bot")

jd_text = st.text_area("Paste Job Description here")
uploaded_files = st.file_uploader("Upload Resumes (PDF)", accept_multiple_files=True, type="pdf")

if st.button("Match Candidates") and jd_text and uploaded_files:
    results = []
    for file in uploaded_files:
        with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
            file.seek(0)
            tmp.write(file.read())
            tmp.flush()
            resume_text = extract_text(tmp.name)
        score = get_match_score(resume_text, jd_text)
        results.append({"Candidate": file.name, "Match %": score})

    results = sorted(results, key=lambda x: x["Match %"], reverse=True)
    st.table(results)