import streamlit as st

# display chat history
def display_chat_history(messages):
    for message in messages:
        role = message["role"]
        content = message["parts"]
        
        if role == "model":
            with st.chat_message("assistant"):
                st.write(content)
        else:
            with st.chat_message(role):
                st.write(content)
