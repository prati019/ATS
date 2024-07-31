import streamlit as st
import google.generativeai as genai
import os
import PyPDF2 as pdf
from dotenv import load_dotenv
import json

load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))


def get_gemini_response(input_text):
    model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content(input_text)
    return response.text


def extract_text_from_pdf(uploaded_file):
    reader = pdf.PdfReader(uploaded_file)
    text = ""
    for page in range(len(reader.pages)):
        text += reader.pages[page].extract_text()
    return text


input_prompt_template = """
You are an skilled ATS (Applicant Tracking System) scanner with a deep understanding of data science and ATS functionality, 
your task is to evaluate the resume against the provided job description. Provide the percentage of match (CV Score) if the resume matches 
the job description. Identify areas for improvement in the resume. Suggest skills that need improvement.

Provide your response in the following JSON format:
{{
    "CV Score": "%",
    "Areas of Improvement": [],
    "Skills Improvement Suggestions": [],
}}

resume: {resume_text}
description: {job_description}

"""

st.title("ATS")

job_description = st.text_area("Job Description")
uploaded_file = st.file_uploader(
    "Upload Your Resume", type="pdf", help="Please upload the PDF"
)

if st.button("Submit"):
    if uploaded_file is not None and job_description:
        resume_text = extract_text_from_pdf(uploaded_file)
        input_prompt = input_prompt_template.format(
            resume_text=resume_text, job_description=job_description
        )
        response = get_gemini_response(input_prompt)

        try:
            response_data = json.loads(response)
            st.subheader("ATS Evaluation Result")
            st.write(f"**CV Score:** {response_data['CV Score']}")
            st.write(
                f"**Areas of Improvement:** {', '.join(response_data['Areas of Improvement'])}"
            )
            st.write(
                f"**Skills Improvement Suggestions:** {', '.join(response_data['Skills Improvement Suggestions'])}"
            )
        except json.JSONDecodeError:
            st.error("Error parsing the response from the API. Please try again.")
    else:
        st.error("Please upload a resume and enter a job description.")
