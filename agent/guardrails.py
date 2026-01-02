def validate_output(text: str):
    banned_phrases = [
        "I have 10 years of experience",
        "expert in everything"
    ]
    for phrase in banned_phrases:
        if phrase.lower() in text.lower():
            raise ValueError("Hallucinated experience detected")
