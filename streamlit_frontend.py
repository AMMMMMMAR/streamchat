import streamlit as st
import requests
import uuid

# Page config
st.set_page_config(
    page_title="AI Chatbot",
    page_icon="🤖",
    layout="centered"
)

# API endpoint
API_URL = "http://localhost:8000"

# Initialize session state
if "messages" not in st.session_state:
    st.session_state.messages = []

if "session_id" not in st.session_state:
    st.session_state.session_id = str(uuid.uuid4())

# Title and description
st.title("🤖 AI Chatbot")
st.markdown("Powered by Google Gemini API")

# Sidebar
with st.sidebar:
    st.header("Settings")
    
    if st.button("Clear Chat History"):
        try:
            requests.delete(f"{API_URL}/chat/{st.session_state.session_id}")
            st.session_state.messages = []
            st.session_state.session_id = str(uuid.uuid4())
            st.success("Chat history cleared!")
            st.rerun()
        except Exception as e:
            st.error(f"Error clearing chat: {str(e)}")
    
    st.markdown("---")
    st.markdown("### About")
    st.markdown("This chatbot uses:")
    st.markdown("- **FastAPI** for the backend")
    st.markdown("- **Streamlit** for the frontend")
    st.markdown("- **Google Gemini API** for AI responses")

# Display chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat input
if prompt := st.chat_input("What would you like to know?"):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    # Display user message
    with st.chat_message("user"):
        st.markdown(prompt)
    
    # Get bot response
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        
        try:
            # Call the API
            response = requests.post(
                f"{API_URL}/chat",
                json={
                    "message": prompt,
                    "session_id": st.session_state.session_id
                }
            )
            
            if response.status_code == 200:
                bot_response = response.json()["response"]
                message_placeholder.markdown(bot_response)
                
                # Add assistant response to chat history
                st.session_state.messages.append(
                    {"role": "assistant", "content": bot_response}
                )
            else:
                error_msg = f"Error: {response.status_code} - {response.text}"
                message_placeholder.error(error_msg)
                
        except requests.exceptions.ConnectionError:
            message_placeholder.error(
                "⚠️ Cannot connect to the API. Make sure the FastAPI server is running on http://localhost:8000"
            )
        except Exception as e:
            message_placeholder.error(f"An error occurred: {str(e)}")

# Footer
st.markdown("---")
st.markdown(
    "<p style='text-align: center; color: gray;'>Made with ❤️ using FastAPI, Streamlit & Gemini</p>",
    unsafe_allow_html=True
)