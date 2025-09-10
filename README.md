# 🧠 IntervAgent – Agentic AI Mock Interviewer + Feedback Generator

**IntervAgent** is an agentic AI-powered system that simulates real-world interviews, provides constructive feedback, and generates ratings for candidate answers. It helps users prepare efficiently for technical and HR interviews with adaptive questioning and actionable insights.

---

## Features
- **Role-Based Question Generation:** Generates challenging and relevant interview questions tailored to the role.  
- **Answer Feedback:** Provides detailed feedback on strengths, weaknesses, and improvement suggestions.  
- **Rating System:** Gives a rating out of 5 along with a concise justification.  
- **Session Memory:** Maintains the current question for multi-step interview simulation.  
- **User-Friendly Interface:** Built using Streamlit for easy interaction.

---

## Architecture & Design
- **Workflow:**  
  1. User inputs role/job profile.  
  2. AI generates an interview question.  
  3. User submits an answer.  
  4. AI provides feedback and rating.  
- **Backend:** Uses OpenAI GPT-3.5 or compatible models for question generation, feedback, and rating.  
- **Implementation Highlights:**  
  - Streamlit front-end for interactive UI  
  - Modular prompts for question generation, feedback, and scoring  
  - Error handling for robust API interactions  

---

## Technologies Used
- **Frontend/UI:** Streamlit  
- **AI Model:** OpenAI GPT-3.5 or Groq-compatible LLaMA models  
- **Language:** Python  
- **Version Control:** Git/GitHub  

