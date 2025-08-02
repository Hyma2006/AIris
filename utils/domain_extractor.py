# File: utils/domain_classifier.py

def extract_domain(text):
    text = text.lower()
    if "data science" in text or "pandas" in text or "numpy" in text:
        return "datascience"
    elif "react" in text or "html" in text or "css" in text or "javascript" in text:
        return "webdevelopment"
    elif "machine learning" in text or "tensorflow" in text or "scikit" in text:
        return "machinelearning"
    else:
        return "general"
