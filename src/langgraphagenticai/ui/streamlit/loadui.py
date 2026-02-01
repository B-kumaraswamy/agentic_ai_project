import streamlit as st 
import os 
from src.langgraphagenticai.ui.uiconfigfile import Config 

class LoadStreamlitUI:
    def __init__(self):
        self.config = Config()
        self.user_controls = {}

    def load_streamlit_ui(self):
        st.set_page_config(layout="wide", page_title=self.config.get_page_title())
        st.header(self.config.get_page_title())
        st.session_state.timeframe = "" 
        st.session_state.isFetchButtonClicked = False

        with st.sidebar:
            # Get options from config
            llm_options = self.config.get_llm_options() 
            usecase_options = self.config.get_usecase_options()

            # LLM selection 
            self.user_controls["selected_llm"] = st.selectbox("Select LLM", llm_options)

            if self.user_controls["selected_llm"] == "Groq":
                # Model Selections
                model_options = self.config.get_groq_model_options()
                self.user_controls["selected_groq_model"] = st.selectbox("Select Model", model_options)
                self.user_controls["GROQ_API_KEY"] = st.session_state["GROQ_API_KEY"] = st.text_input("API Key", type="password")

                if not self.user_controls["GROQ_API_KEY"]:
                    st.warning("Please enter your GROQ API KEY. Don't have? refer : https://console.groq.com/keys")

            # Usecase Selection 
            self.user_controls["selected_usecase"] = st.selectbox("Select Usecase", usecase_options)

            if self.user_controls["selected_usecase"].strip() == "Chatbot with web" or self.user_controls["selected_usecase"].strip() == "AI News":
                os.environ["TAVILY_API_KEY"] = self.user_controls["TAVILY_API_KEY"] = st.session_state["TAVILY_API_KEY"] = st.text_input("TAVILI API KEY", type="password")

                if not self.user_controls["TAVILY_API_KEY"]:
                    st.warning("Please enter your TAVILI API KEY. Don't have? refer : https://app.tavily.com/home")

            if self.user_controls["selected_usecase"].strip() == "AI News":
                st.subheader("AI News Explorer")

                with st.sidebar:
                    time_frame = st.selectbox("Select Time Frame", ["Daily", "Weekly", "Monthly"], index = 0)

                if st.button("Fetch Latest AI News", use_container_width=True):
                    # st.session_state["fetch_latest_ai_news"] = True
                    st.session_state.timeframe = time_frame
                    st.session_state.isFetchButtonClicked = True
        
        return self.user_controls
                    