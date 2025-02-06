def get_greeting_prompt():
    return """
    You are a hiring assistant chatbot for TalentScout, a tech recruitment agency.
    Your job is to greet candidates and explain the screening process.
    """

def get_questions_prompt(tech_stack):
    return f"""
    Generate 3-5 technical interview questions for a candidate skilled in: {', '.join(tech_stack)}.
    Make sure the questions assess proficiency and problem-solving skills.
    """
