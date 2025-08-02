# File: models/question_generator.py

def generate_questions(domain):
    domain = domain.lower()
    rule_based_questions = {
        "datascience": [
            "What are the steps in a data science workflow?",
            "How do you handle missing data in a dataset?",
            "Explain the difference between supervised and unsupervised learning.",
            "What is overfitting and how can you prevent it?",
            "Which libraries do you use most in data science projects and why?"
        ],
        "webdevelopment": [
            "What is the difference between HTML and HTML5?",
            "Explain how the DOM works in JavaScript.",
            "What is the difference between REST and GraphQL?",
            "How do you optimize a website for performance?",
            "What’s your experience with frontend frameworks like React or Angular?"
        ],
        "machinelearning": [
            "Explain the bias-variance tradeoff.",
            "What is gradient descent and how does it work?",
            "When would you choose a decision tree over a neural network?",
            "How do you evaluate the performance of a machine learning model?",
            "What are some common challenges in training deep learning models?"
        ]
    }
    return rule_based_questions.get(domain, ["Sorry, no questions available for this domain."])
