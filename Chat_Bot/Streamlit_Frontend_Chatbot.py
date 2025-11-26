import streamlit as st
from Langgraph_Backend_Chatbot import workflow
from langchain_core.messages import HumanMessage , BaseMessage
from langchain_groq import ChatGroq

config={'configurable':{'thread_id':'thread-1'}}

if 'message_history' not in st.session_state:
    st.session_state['message_history'] = []

# Loading the Conversation History
for message in st.session_state['message_history']:
    with st.chat_message(message['role']):
        st.text(message['content'])

user_input = st.chat_input('user')

if user_input:

    st.session_state['message_history'].append({'role':'user','content':user_input})

    with st.chat_message('user'):
        st.text(user_input)

    def stream_response():
        for message_chunk, metadata in workflow.stream(
            {"messages":[HumanMessage(content=user_input)]},
            config={'configurable':{'thread_id':'thread-1'}},
            stream_mode='messages'
        ):
            # message_chunk is a BaseMessage (AIMessage)
            yield message_chunk.content

    with st.chat_message('assistant'):
        ai_message = st.write_stream(stream_response())

    st.session_state['message_history'].append({'role':'assistant','content':ai_message})