import streamlit as st
from langchain_ollama import OllamaLLM

# Initialize the Llama model
model = OllamaLLM(model="llama3.2")

# Header for the application
st.header("0 Llama's AI🦙")

# Introduction message
st.write("""
Hello I am 0 Llama's AI🦙
I am AI made with Ollama and Llama 3.2.
I hope you use me well
""")

# Initialize session state to store history of multiple conversations
if 'conversations' not in st.session_state:
    st.session_state.conversations = {}
    st.session_state.counter = 0  # Track conversation branches

# Function to add a new conversation
def add_conversation():
    st.session_state.counter += 1
    conversation_id = f"chat_{st.session_state.counter}"
    st.session_state.conversations[conversation_id] = []

# User interface to select or add conversations
conversation_id = st.selectbox("Select a Conversation:", list(st.session_state.conversations.keys()) + ["New Chat"])

if conversation_id == "New Chat":
    add_conversation()
    conversation_id = f"chat_{st.session_state.counter}"

# Display the past conversation history in a scrollable area
if st.session_state.conversations:
    st.write(f"### Conversation History for {conversation_id}:")
    conversation_history = st.session_state.conversations[conversation_id]
    for user_question, ai_response in conversation_history:
        st.write(f"User🙂: {user_question}")
        st.write(f"AI💻: {ai_response}")

# Create a form for user input at the bottom
question = st.text_input("🦙>>>")
   

if question:
    result = model.invoke(input=question)
    # Store the question and result in the selected conversation history
    st.session_state.conversations[conversation_id].append((question, result))

    # Optionally display the new user question and AI response immediately after submission
    st.write(f"User🙂: {question}")
    st.write(f"AI💻: {result}")