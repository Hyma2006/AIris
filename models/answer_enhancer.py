
# File: models/answer_enhancer.py

def enhance_answer(question, answer, domain):
    # Simple rule-based enhancement
    if not answer.strip():
        return "Your answer was empty. Please try again."

    return (
        f"**Question:** {question}\n\n"
        f"**Your Answer:** {answer}\n\n"
        f"**Suggested Improvement:**\n"
        f"In the context of {domain}, try to add real-world examples, tools or methods. "
        f"Make sure your answer clearly reflects your experience and understanding of the topic."
    )

