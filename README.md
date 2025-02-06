# TalentScout - Hiring Assistant Chatbot

Project Overview

TalentScout is an AI-powered Hiring Assistant chatbot designed to streamline the job application process. It collects candidate details, analyzes their tech stack, and generates relevant technical questions to assess their expertise. The chatbot helps recruiters evaluate applicants efficiently by automating the initial screening process.

Installation Instructions

Follow these steps to set up and run the application locally:

Prerequisites:

Python 3.10+

OpenAI API key

Streamlit

Required Python dependencies

Steps:

Clone the Repository

git clone https://github.com/your-repo/talent-scout.git
cd talent-scout

Create a Virtual Environment (Optional but recommended)

python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

Install Dependencies

pip install -r requirements.txt

Set Up OpenAI API Key

Create a .env file in the project root and add:

OPENAI_API_KEY=your-api-key-here

Run the Application

streamlit run app.py

Usage Guide

Open the application in your browser.

Fill in the required candidate details (name, email, experience, tech stack, etc.).

Submit the form to generate technical questions based on the provided tech stack.

Answer the generated questions.

Upon submission, receive a confirmation message: "Thank you for your time! Our team will review your responses and get back to you."

Technical Details

Framework: Streamlit (for UI)

AI Model: OpenAI GPT (for question generation)

Key Libraries:

streamlit - UI framework

openai - GPT-based question generation

python-dotenv - Environment variable management

Prompt Design

The chatbot uses structured prompts to achieve two main goals:

Information Gathering: A system prompt is designed to extract relevant candidate information based on user input.

Question Generation: Once tech stack details are collected, another prompt is used to generate role-specific technical questions.

Challenges & Solutions

1. API Rate Limit & Quota Exceeded

Problem: OpenAI API rate limits caused the chatbot to fail in generating questions.

Solution: Implemented error handling to show fallback messages like: "Please Describe Your Expertise in @data you give in the tech stack."

2. Handling Empty or Invalid Tech Stack Inputs

Problem: Users sometimes enter incomplete or vague tech stack details.

Solution: Added validation checks and warning messages prompting users to provide meaningful input.

3. UI Enhancements for Better User Experience

Problem: The initial version had no input fields for answers.

Solution: Implemented text areas for each question, allowing users to submit responses within the chatbot interface.

Developed by

Gunupuru Vamsi
