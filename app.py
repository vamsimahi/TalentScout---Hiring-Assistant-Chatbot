import streamlit as st
import os
import openai
from dotenv import load_dotenv
from prompts import get_greeting_prompt, get_questions_prompt
from utils import extract_candidate_info, generate_questions

# Load API Key securely
openai.api_key = os.getenv("OPENAI_API_KEY", "sk-xxx")  # Replace with your API key

# Streamlit UI
st.set_page_config(page_title="TalentScout - Hiring Assistant", layout="wide")

st.title("🤖 TalentScout Hiring Assistant")
st.write("Welcome! I'm here to assist with your job application. Let's get started!")

# Initialize session state
if "stage" not in st.session_state:
    st.session_state.stage = "gather_info"
    st.session_state.candidate_info = {}
    st.session_state.tech_questions = []
    st.session_state.answers_submitted = False  # Track answer submission

# Collect Candidate Information
if st.session_state.stage == "gather_info":
    with st.form(key="candidate_form"):
        name = st.text_input("Full Name")
        email = st.text_input("Email Address")
        phone = st.text_input("Phone Number")
        experience = st.number_input("Years of Experience", min_value=0, step=1)
        position = st.text_input("Desired Position(s)")
        location = st.text_input("Current Location")
        tech_stack = st.text_area("Tech Stack (e.g., Python, Django, MySQL, Docker)")
        submit = st.form_submit_button("Submit")
    
    if submit:
        st.session_state.candidate_info = {
            "name": name,
            "email": email,
            "phone": phone,
            "experience": experience,
            "position": position,
            "location": location,
            "tech_stack": tech_stack.split(", ") if tech_stack else []
        }
        st.session_state.stage = "ask_questions"

# Generate Technical Questions
if st.session_state.stage == "ask_questions":
    tech_stack = st.session_state.candidate_info.get("tech_stack", [])
    if tech_stack:
        questions = generate_questions(tech_stack)
        if isinstance(questions, list):
            st.session_state.tech_questions = questions
            st.session_state.stage = "show_questions"
        else:
            st.error("Error generating questions. Please try again later.")
    else:
        st.warning("Please enter a valid Tech Stack before proceeding.")

# Display Technical Questions with Answer Fields
if st.session_state.stage == "show_questions":
    st.write("### Technical Questions")
    answers = {}
    
    with st.form(key="answers_form"):
        for idx, question in enumerate(st.session_state.tech_questions):
            st.write(f"**Q{idx+1}:** {question}")
            answers[f"q{idx+1}"] = st.text_area(f"Your Answer for Q{idx+1}", key=f"answer_{idx+1}")
        submit_answers = st.form_submit_button("Submit Answers")
    
    if submit_answers:
        st.session_state.answers = answers
        st.session_state.answers_submitted = True  # Mark answers as submitted
        st.session_state.stage = "end_convo"

# End Conversation after Answer Submission
if st.session_state.stage == "end_convo" and st.session_state.answers_submitted:
    st.success("Thank you for your time! Our team will review your responses and get back to you.")