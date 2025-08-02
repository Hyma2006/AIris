# File: app.py

import streamlit as st
from utils.resume_parser import extract_text_from_pdf
from utils.domain_classifier import extract_domain
from utils.speech_to_text import transcribe_from_microphone
from models.question_generator import generate_questions
from models.answer_enhancer import enhance_answer

# ------------------ Page Configuration ------------------
st.set_page_config(page_title="AI InterviewBuddy", layout="wide")

# ------------------ Custom Styling ------------------
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Quicksand:wght@500&family=Outfit:wght@600;700&display=swap');

html, body, [class*="css"] {
    font-family: 'Outfit', 'Quicksand', sans-serif;
    background-color: #0d1117;
    color: #d1d5db;
}

.main-container {
    background-color: #161b22;
    padding: 2rem;
    border-radius: 16px;
    margin: 3rem auto;
    max-width: 900px;
    box-shadow: 0 8px 24px rgba(0,0,0,0.4);
}

.app-title {
    font-family: 'Outfit', sans-serif;
    font-size: 3rem;
    text-align: center;
    color: #22c55e;
    margin-bottom: 0.5rem;
}

.subtitle {
    font-size: 1.1rem;
    text-align: center;
    color: #9ca3af;
    margin-bottom: 2rem;
}

.stButton>button {
    background-color: #22c55e;
    color: #0d1117;
    font-weight: bold;
    border-radius: 8px;
    padding: 0.6rem 1.2rem;
    border: none;
    transition: 0.3s ease;
}

.stButton>button:hover {
    background-color: #16a34a;
    transform: scale(1.02);
}

.stTextArea textarea {
    background-color: #1f2937;
    color: #f9fafb;
    border: 1px solid #374151;
    border-radius: 8px;
}

.stSelectbox div {
    background-color: #1f2937 !important;
    color: #f9fafb !important;
}

.stFileUploader {
    background-color: #1f2937;
    padding: 1rem;
    border-radius: 10px;
    border: 1px dashed #4b5563;
}

.stAlert {
    border-radius: 10px;
}
</style>
""", unsafe_allow_html=True)

# ------------------ UI Container ------------------
st.markdown('<div class="main-container">', unsafe_allow_html=True)

# Add Top Illustration like in 2nd image
st.image("https://cdn.pixabay.com/photo/2023/10/12/08/55/interview-8310074_1280.jpg", use_column_width=True)

# Title & Subtitle
st.markdown('<div class="app-title">🤖 AI InterviewBuddy</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Your virtual assistant for mock interviews, powered by GenAI!</div>', unsafe_allow_html=True)

# ------------------ Step 1: Resume Upload ------------------
st.subheader("📄 Upload Resume")
uploaded_file = st.file_uploader("Upload your Resume (PDF)", type=["pdf"])

if uploaded_file:
    with st.spinner("🔍 Extracting text from your resume..."):
        resume_text = extract_text_from_pdf(uploaded_file)
        st.success("✅ Resume parsed successfully!")

    # ------------------ Step 2: Domain Detection ------------------
    st.subheader("🎯 Detected Domain")
    domain = extract_domain(resume_text)
    st.info(f"🔎 Domain identified: `{domain}`")

    # ------------------ Step 3: Generate Questions ------------------
    st.subheader("💬 Interview Questions")
    if st.button("🧠 Generate Interview Questions"):
        with st.spinner("🤖 Generating questions..."):
            questions = generate_questions(domain)

        if questions:
            st.markdown("### 🎓 AI Interview Questions:")
            for i, q in enumerate(questions, 1):
                st.markdown(f"**{i}. {q}**")

            # ------------------ Step 4: Choose a Question ------------------
            st.subheader("🗣️ Choose a Question to Answer")
            selected_question = st.selectbox("Select one to answer:", questions)

            st.markdown("### ✍️ Type Your Answer or Use Voice Input")
            col1, col2 = st.columns(2)

            with col1:
                user_answer = st.text_area("📝 Type your answer here:")

            with col2:
                if st.button("🎤 Or Speak Your Answer"):
                    with st.spinner("🎧 Listening..."):
                        voice_answer = transcribe_from_microphone()
                        st.text_area("📝 Transcribed Voice Answer:", voice_answer)
                        if not user_answer and voice_answer and not voice_answer.lower().startswith("sorry"):
                            user_answer = voice_answer

            # ------------------ Step 5: Enhance Answer ------------------
            if user_answer:
                with st.spinner("✨ AI is enhancing your answer..."):
                    improved = enhance_answer(selected_question, user_answer, domain)
                    st.subheader("✅ Enhanced Answer")
                    st.success(improved)

st.markdown('</div>', unsafe_allow_html=True)

