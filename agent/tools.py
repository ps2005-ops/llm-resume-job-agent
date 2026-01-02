from langchain.tools import tool

@tool
def generate_bullets(text: str) -> str:
    return "\n".join(f"- {line.strip()}" for line in text.split(".")[:5])

@tool
def generate_cover_letter(resume: str, job: str) -> str:
    return f"""
Dear Hiring Manager,

Based on my background:
{resume[:500]}

I am excited about this role:
{job[:500]}
"""
