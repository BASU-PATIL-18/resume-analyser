import streamlit as st
from analysis import analyze_text
st.set_page_config(page_title="Resume Analyzer", page_icon=":mag:", layout="wide")
st.title("Resume Analyzer")
st.header("Upload your resume and job description to analyze your fit for the position.")
st.subheader("Upload your resume (PDF format)")
st.sidebar.subheader("Upload your resume here")
pdf_doc=st.sidebar.file_uploader("Choose a PDF file", type=['pdf'])
st.sidebar.markdown("designed by basu")
job_desc=st.text_area("Enter the job description here", max_chars=20000)
submit=st.button("Analyze Resume")
if submit:
  with st.spinner("Analyzing your resume..."):
    analyze_text(pdf_doc,job_desc)
