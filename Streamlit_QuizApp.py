import streamlit as st

# Set page configuration
st.set_page_config(page_title="Simple Quiz App", layout="centered")

# Title
st.title("🧠 Simple Quiz App")
st.write("Hey Pragyan, Answer this")

# Questions and Answers
questions = {
    "Who sang Baby Song": {
        "options": ["Ed Sheeran", "Justin Bieber", "Taylor swift", "Nelly"],
        "answer": "Justin Bieber"
    },
    "Pop Singer Rose's song": {
        "options": ["APT", "Die with a smile", "Lily", "Bye Bye"],
        "answer": "APT"
    },
    "I always wanted a brother belongs to which movie": {
        "options": ["Cinderella", "Frozen", "Mufasa", "Snowwwhite"],
        "answer": "Mufasa"
    },
    "Who wrote 'Harry Potter and the Goblet of Fire'?": {
        "options": ["Sudhamurthy", "J.K. Rowling", "Harry Potter", "Ron Weasley"],
        "answer": "J.K. Rowling"
    }
}

# Session state to store answers
if "submitted" not in st.session_state:
    st.session_state.submitted = False

user_answers = {}

# Quiz form
with st.form("quiz_form"):
    for idx, (question, data) in enumerate(questions.items()):
        user_answers[question] = st.radio(f"{idx+1}. {question}", options=data["options"], key=question)

    submit = st.form_submit_button("Submit Quiz")

# On submit
if submit:
    st.session_state.submitted = True
    score = 0
    total = len(questions)

    for question, data in questions.items():
        if user_answers[question] == data["answer"]:
            score += 1

    st.success(f"🎉 You scored {score} out of {total}!")

    # Show correct answers
    st.markdown("### ✅ Correct Answers:")
    for question, data in questions.items():
        st.markdown(f"**{question}**: {data['answer']}")

elif st.session_state.submitted:
    st.info("You’ve already submitted the quiz. Refresh to try again.")
