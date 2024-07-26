import streamlit as st
import pandas as pd

# Define the questions and answers
quiz_data = {
    'Question': [
        'How do we identify dictionaries in python',
        'Which value can a Boolean variable take',
        'Which code snippets gives me the first 5 columns and 3 rows of a dataframe',
        'Which loop makes use of the number of elements in a list to iterate through the list',
        'What are lambda functions?'
    ],
    'Options': [
        ['Curly Braces', 'Key Value Pairs', 'All of the Above'],
        ['TRUE', 'NULL', 'String'],
        ['df.iloc[0:3,0:5]', 'df.iloc[0:2,0:6]', 'df.iloc[0:5,0:3]'],
        ['Nested Loop', 'For Loop', 'While Loop'],
        ['A math equation', 'A data structure', 'Anonymous functions in python']
    ],
    'Answer': ['All of the Above', 'TRUE', 'df.iloc[0:3,0:5]', 'For Loop', 'Anonymous functions in python']
}

def main():
    st.title("Python for Financial Data Analysis Exam")
    
    if 'submitted' not in st.session_state:
        st.session_state.submitted = False
        st.session_state.score = 0

    df = pd.DataFrame(quiz_data)
    
    if not st.session_state.submitted:
        display_quiz(df)
    else:
        display_results(df)

def display_quiz(df):
    st.write("Answer all questions and click 'Submit' when you're done.")
    
    user_answers = []
    for i, row in df.iterrows():
        st.write(f"Question {i+1}: {row['Question']}")
        answer = st.radio("Select your answer:", row['Options'], key=f"q{i}")
        user_answers.append(answer)
    
    if st.button("Submit"):
        st.session_state.submitted = True
        st.session_state.score = sum([ua == ca for ua, ca in zip(user_answers, df['Answer'])])
        st.rerun()

def display_results(df):
    score = st.session_state.score
    total_questions = len(df)
    percentage = (score / total_questions) * 100
    
    st.write(f"Quiz completed! Your score: {score}/{total_questions} ({percentage:.2f}%)")
    
    if percentage >= 80:
        st.balloons()
        st.success("Congratulations! You passed the quiz!")
        st.info("Email the code 'qzzel6qyed' along with your full name to michael@whypred.com to receive your completion certificate.")
        st.write("Review of correct answers:")
        for i, row in df.iterrows():
            st.write(f"Question {i+1}: {row['Question']}")
            st.write(f"Correct answer: {row['Answer']}")
            st.write("---")
    else:
        st.warning("You need to score 80% or higher to pass the quiz.")
    
    
    
    if st.button("Retake Quiz"):
        st.session_state.submitted = False
        st.session_state.score = 0
        st.rerun()

if __name__ == "__main__":
    main()