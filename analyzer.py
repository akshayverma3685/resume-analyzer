import re

# Example skill set (tum isme aur skills add kar sakte ho)
SKILLS = ["python", "java", "c++", "sql", "machine learning", "data analysis", "cloud", "git"]

def analyze_resume(text):
    text_lower = text.lower()
    found_skills = [skill for skill in SKILLS if skill in text_lower]
    missing_skills = [skill for skill in SKILLS if skill not in text_lower]

    # Simple ATS score (based on skills found)
    score = int((len(found_skills) / len(SKILLS)) * 100)

    analysis = {
        "found": found_skills,
        "missing": missing_skills,
        "score": score,
    }
    return analysis
