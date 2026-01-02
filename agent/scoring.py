def fit_score(resume_text: str, job_text: str) -> float:
    resume_words = set(resume_text.lower().split())
    job_words = set(job_text.lower().split())
    overlap = resume_words.intersection(job_words)
    return round(len(overlap) / max(len(job_words), 1), 2)
