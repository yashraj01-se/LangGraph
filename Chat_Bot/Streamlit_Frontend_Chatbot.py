import streamlit as st
from Langgraph_Backend_Chatbot import workflow
from langchain_core.messages import HumanMessage , BaseMessage
from langchain_groq import ChatGroq

thread_id="1"
configuration={'configurable':{'thread_id':thread_id}}

if 'message_history' not in st.session_state: ## St.session_state is basically a dictionary how data do not get delete at the time we press enter again...
    st.session_state['message_history']=[]

#Loading the Conversation History
for message in st.session_state['message_history']:
    with st.chat_message(message['role']):
        st.text(message['content'])

user_input=st.chat_input('user')

if user_input:

    #adding to the History first:
    st.session_state['message_history'].append({'role':'user','content':user_input})
    with st.chat_message('user'):
        st.text(user_input)
    

    response=workflow.invoke({"messages":[HumanMessage(content=user_input)]},config=configuration)
    output=response['messages'][-1].content
    st.session_state['message_history'].append({'role':'assistant','content':output})
    with st.chat_message('assistant'):
        st.text(output)