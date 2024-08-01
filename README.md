# ATS

An Applicant Tracking System (ATS) that uses the Google Gemini Pro Vision API to analyze resumes and compare them with job descriptions. The system provides a CV score, suggests improvements and offers skill enhancement recommendations.

##Project link
https://github.com/prati019/ATS

## Install
Python 3.9 or higher
Anaconada

## Steps
1. Install necessary libraries
    - `pip install requirements.txt`
2. Set up your environment variables:
    - Create a `.env` file in the project directory.
    - Add your Google API key: `GOOGLE_API_KEY=your_api_key_here`
3. Run the Streamlit app:
    - `streamlit run app.py`

## Usage
1. Paste the job description into the provided text area.
2. Upload your resume in PDF format.
3. Click 'Submit' to receive an evaluation of your resume, including CV score, areas for improvement, skills improvement suggestions.

## Features
Resume Analysis: Extracts and evaluates the content of uploaded resumes.
Job Description Matching: Compares resumes with job descriptions and provides a CV score.
Improvement Suggestions: Identifies areas for improvement and suggests skills to enhance.
