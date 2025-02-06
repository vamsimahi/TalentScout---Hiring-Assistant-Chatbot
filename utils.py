import openai
import time
import random

def extract_candidate_info(response_text):
    """
    Process the candidate's input and return structured information.
    """
    # Simple processing for now
    return response_text.split("\n")


def generate_questions(tech_stack):
    """Generates technical questions based on tech stack without OpenAI API when quota is exceeded."""
    
    # Predefined questions for common technologies
    question_bank = {
        "Python": [
            "What are Python's key data structures?",
            "Explain the difference between lists and tuples in Python.",
            "What is the purpose of Python's `__init__` method?",
            "What are Python decorators and how do they work?",
            "Explain the concept of Python's list comprehensions."
        ],
        "Django": [
            "What is Django ORM?",
            "How do you create a model in Django?",
            "Explain Django's MVT architecture.",
            "What is middleware in Django?",
            "How do you implement authentication in Django?"
        ],
        "MySQL": [
            "What is the difference between MySQL and PostgreSQL?",
            "Explain normalization in databases.",
            "How do you optimize a MySQL query?",
            "What are ACID properties in MySQL?",
            "What are joins in SQL, and how do they work?"
        ],
        "Docker": [
            "What is Docker, and why is it used?",
            "Explain the difference between Docker images and containers.",
            "How do you write a Dockerfile?",
            "What is Docker Compose, and how is it used?",
            "How do you manage container networking in Docker?"
        ],
        "JavaScript": [
            "What are closures in JavaScript?",
            "Explain the event loop in JavaScript.",
            "What is the difference between `let`, `const`, and `var`?",
            "What is a promise in JavaScript?",
            "What are higher-order functions in JavaScript?"
        ],
        "React": [
            "What is React, and how does it work?",
            "What is JSX in React?",
            "Explain the concept of components in React.",
            "What is the Virtual DOM in React?",
            "What are React hooks, and how do they work?"
        ],
        "Java": [
            "What is the difference between `==` and `===` in Java?",
            "Explain the concept of inheritance in Java.",
            "What are Java streams, and how do they work?",
            "What is polymorphism in Java?",
            "What are Java annotations and how are they used?"
        ],
        "Ruby": [
            "What is Ruby on Rails?",
            "Explain the difference between symbols and strings in Ruby.",
            "What are Ruby modules, and how are they used?",
            "What is a block in Ruby?",
            "Explain Ruby's garbage collection mechanism."
        ],
        "Node.js": [
            "What is Node.js and how does it work?",
            "What are streams in Node.js?",
            "Explain event-driven programming in Node.js.",
            "What is the role of the package manager `npm`?",
            "How do you handle errors in Node.js?"
        ],
        "Angular": [
            "What is Angular and what are its core features?",
            "What is two-way data binding in Angular?",
            "What is dependency injection in Angular?",
            "What are directives in Angular?",
            "How do you handle forms in Angular?"
        ]
    }
    
    questions = []
    for tech in tech_stack:
        if tech in question_bank:  # This is case-sensitive
            questions.extend(random.sample(question_bank[tech], min(3, len(question_bank[tech]))))  # Pick 3 random questions
    
    # If no questions are generated, show a default message
    if not questions:
        questions.append("No specific technical questions available. Please describe your expertise.")
    
    return questions
