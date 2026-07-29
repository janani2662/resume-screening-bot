# 🤖 AI Resume Screening Bot

An AI-powered tool that automatically screens and ranks candidate resumes 
against a given Job Description using Natural Language Processing (NLP) 
and TF-IDF cosine similarity scoring.

## 🔗 Live Demo
👉 [Try the app here](https://resume-screening-bot-tr2ovookxbyqkxzjyhg9ad.streamlit.app/)

## Features
- 📄 Upload multiple resumes (PDF format)
- 📝 Paste any Job Description
- 🎯 Get instant match percentage scores
- 📊 Automatically ranks candidates by relevance

## Tech Stack
- Python
- Streamlit (UI)
- PyPDF2 (Resume parsing)
- scikit-learn (TF-IDF & Cosine Similarity)

## How to Run Locally
1. Clone this repository
2. Install dependencies: `pip install -r requirements.txt`
3. Run: `streamlit run app.py`

## Future Improvements
- Named Entity Recognition (NER) for skill extraction
- Semantic matching using sentence embeddings
- Bias-free candidate screening