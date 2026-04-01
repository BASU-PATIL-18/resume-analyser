import os# This code is for setting up the environment and configuring the Google Generative AI model. It loads the API key from a .env file and initializes the model for use in generating content.

import streamlit as st
from dotenv import load_dotenv # Make sure to install python-dotenv if you haven't already: pip install python-dotenv
load_dotenv()# Load environment variables from a .env file
import google.generativeai as genai
from pdf import extractpdf
key = os.getenv("google_api_key")
genai.configure(api_key=key)
model=genai.GenerativeModel("gemini-2.5-flash")
def analyze_text(pdf_doc,job_description):
  if pdf_doc is not None:
    pdf_text=extractpdf(pdf_doc)
    st.write("Extracted Text from PDF")
  else:
    st.write("No PDF document provided.")
  ats_score=model.generate_content(f"Please analyze the following resume text and job description, and provide an ATS score based on how well the resume matches the job description. Resume Text: {pdf_text} Job Description: {job_description}")
  prob_score=model.generate_content(f'compare the resume{pdf_text} with the job description {job_description} and provide a probability score of how likely the candidate is to be selected for an interview based on the content of the resume and its relevance to the job description.')
  good_fit=model.generate_content(f'compare the resume{pdf_text} with the job description {job_description} and provide a brief explanation of why the candidate is a good fit or not for the position based on the content of the resume and its relevance to the job description and suggest improvements.')

  swot_analysis=model.generate_content(f'compare the resume{pdf_text} with the job description {job_description} and provide a SWOT analysis of the candidate based on the content of the resume and its relevance to the job description, highlighting the candidate\'s strengths, weaknesses, opportunities, and threats in relation to the position.') 
  return ats_score,prob_score,good_fit,swot_analysis