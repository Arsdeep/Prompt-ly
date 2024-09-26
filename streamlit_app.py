import streamlit as st
import google.generativeai as genai
from helper.display_chat import display_chat_history

genai.configure(api_key = st.secrets.GEMINI_API_KEY)
model = genai.GenerativeModel('gemini-1.5-flash')

# streamlit web app configuration
st.set_page_config(
    page_title="Promptly",
    page_icon="🛠️",
    layout="centered",
)

# streamlit page title
st.title("🤖 COSTAR Generator")
st.subheader("Powered by Google's Gemini✨")

# initialize chat history in streamlit session state
if "chat_history" not in st.session_state:
    st.session_state.chat_history = [
        {"role": "user", "parts": st.secrets.COSTAR_PROMPT},
    ]

display_chat_history(st.session_state.chat_history[1:])

chat = model.start_chat(history = st.session_state.chat_history)

user_prompt = st.chat_input("Enter your prompt")


if user_prompt:
    
    st.session_state.chat_history.append({"role":"user","parts": user_prompt})
    
    display_chat_history([st.session_state.chat_history[-1]])

    gemini_response = chat.send_message(user_prompt).text

    st.session_state.chat_history.append({"role":"model", "parts": gemini_response})
    
    display_chat_history([st.session_state.chat_history[-1]])