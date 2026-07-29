# Set of candidate skills
candidate_skills = {"Python", "Git", "SQL", "Docker", "Linux", "FastAPI"}

# Required skills for Backend Developer
required_skills = {"Python", "SQL", "Docker"}

print("--- Backend Developer Skill Check ---")

# Method 1: Checking condition using 'in' operator inside loop
missing_skills = []

for skill in required_skills:
    if skill not in candidate_skills:
        missing_skills.append(skill)

if not missing_skills:
    print("The candidate meets all Backend requirements! (Python, SQL, Docker)")
else:
    print("The candidate is missing:", missing_skills)