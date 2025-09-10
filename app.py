import streamlit as st
import openai

st.set_page_config(page_title="Agentic Mock Interviewer", layout="centered")
st.title("🧠 Agentic Mock Interviewer + Feedback Generator")

openai.api_key = st.secrets["GROQ_API_KEY"]
openai.api_base = "https://api.groq.com/openai/v1"

st.markdown("**Step 1:** Enter the role you're preparing for")
job_role = st.text_input("Enter Role (e.g., Data Scientist at Google)")

question = ""
if st.button("🎤 Generate Interview Question"):
    try:
        prompt = f"""You are an expert interviewer. 
        Ask a challenging and relevant interview question for the role: {job_role}.
        """
        response = openai.ChatCompletion.create(
            model="llama-3.1-8b-instant",  # Or try llama3-70b / mixtral
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7
        )
        question = response.choices[0].message.content
        st.session_state["question"] = question

        st.markdown(f"""### 🗨️ Interview Question:
{question}""")

    except Exception as e:
        st.error(f"❌ Error generating question: {str(e)}")


if "question" in st.session_state:
    st.markdown("**Step 3:** Write your answer below")
    user_answer = st.text_area("Your Answer", height=200)

    if st.button("📝 Generate Feedback"):
        try:
            # Feedback Prompt
            feedback_prompt = f"""You are a professional interviewer. 
            Here is the question and the candidate's answer.

            Question: {st.session_state['question']}
            Answer: {user_answer}

            Provide **constructive feedback in bullet points**, including:
            - Strengths
            - Weaknesses
            - Suggestions for improvement
            """

            feedback = openai.ChatCompletion.create(
                model="llama-3.1-8b-instant",
                messages=[{"role": "user", "content": feedback_prompt}],
                temperature=0.7
            )

            st.subheader("📋 AI Feedback")
            st.markdown(feedback.choices[0].message.content)

            # Rating Prompt
            rating_prompt = f"""You are an expert interviewer. 
            Based on the following question and candidate's answer, 
            give a rating out of 5 (5 = excellent, 1 = poor) with a one-line justification.

            Question: {st.session_state['question']}
            Answer: {user_answer}

            Respond in this format:
            Rating: X/5
            Reason: <one-line justification>
            """

            rating_response = openai.ChatCompletion.create(
                model="llama-3.1-8b-instant",
                messages=[{"role": "user", "content": rating_prompt}],
                temperature=0.7
            )

            st.subheader("⭐ Final Rating")
            st.markdown(rating_response.choices[0].message.content)

        except Exception as e:
            st.error(f"❌ Error generating feedback: {str(e)}")
