import os
import streamlit as st
from langchain_groq import ChatGroq

class GroqLLM:
    def __init__(self, user_controls_input):
        self.user_controls_input = user_controls_input

    def get_llm_model(self):
        groq_api_key = self.user_controls_input.get("GROQ_API_KEY")
        selected_groq_model = self.user_controls_input.get("selected_groq_model")

        if not groq_api_key:
            st.error("Groq API key is missing.")
            st.stop()
        if not selected_groq_model:
            st.error("Model selection is missing.")
            st.stop()

        try:
            st.write("🔧 Initializing model:", selected_groq_model)
            llm = ChatGroq(api_key=groq_api_key, model=selected_groq_model)
            return llm

        except Exception as e:
            import traceback
            st.error("❌ LLM model could not be initialized.")
            st.code(traceback.format_exc(), language="python")
            st.stop()
