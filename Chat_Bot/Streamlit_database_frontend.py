import streamlit as st
from Langgraph_database_backend import workflow,retreive_all_threads
from langchain_core.messages import HumanMessage , BaseMessage
from langchain_groq import ChatGroq
import uuid

groq = ChatGroq(model="llama-3.1-8b-instant")

######################### Utility Function ##############################

def generate_id():
    thread_id=str(uuid.uuid4())
    return thread_id

def reset_chat():
    thread_id=generate_id()
    st.session_state['thread_id']=thread_id
    add_thread(st.session_state['thread_id'])
    st.session_state['message_history']=[]

def add_thread(thread_id):
    # Check if thread already exists
    for chat in st.session_state['chat_list']:
        if chat["id"] == str(thread_id):
            return  # already exists

    # Add new thread as dict ONLY
    st.session_state['chat_list'].append({
        "id": str(thread_id),
        "title": "Current Conversation"
    })

def load_coversation(thread_id):
    state = workflow.get_state(config={'configurable': {'thread_id': thread_id}})
    return state.values.get('messages', [])



def generate_title_from_llm(msg: str) -> str:
    prompt = (
        "Create a short, concise title (4 to 6 words) summarizing this message:\n"
        f"{msg}\n\nTitle:"
    )
    response = groq.invoke(input=prompt)
    return response.content.strip()

########################## Session Setup ############################

if 'message_history' not in st.session_state:
    st.session_state['message_history'] = []

if 'thread_id' not in st.session_state:
    st.session_state['thread_id']=generate_id()

if 'chat_list' not in st.session_state:
    st.session_state['chat_list']=retreive_all_threads()

# Normalize chat_list (convert strings → dicts)
normalized_list = []
for chat in st.session_state['chat_list']:
    if isinstance(chat, str):
        normalized_list.append({"id": chat, "title": "Conversation"})
    else:
        normalized_list.append(chat)

st.session_state['chat_list'] = normalized_list

### At the time of reloading ###
add_thread(st.session_state['thread_id'])

############################ SidebarUI #####################################

st.sidebar.title("LangGraph Chatbot")

### When New Chat is clicked:
if st.sidebar.button("New Chat",key="new-chat-btn"):
    reset_chat()

st.sidebar.header("My Conversations")

for chat_data in st.session_state['chat_list']:
    if st.sidebar.button(chat_data["title"],key=f"chat-btn-{chat_data['id']}"):
        st.session_state['thread_id']=chat_data["id"]
        messages=load_coversation(chat_data["id"])


        temp_message=[]

        for msg in messages:
            if isinstance(msg,HumanMessage):
                role='user'
            else:
                role='assistant'
            temp_message.append({'role':role,'content':msg.content})
        
        st.session_state['message_history']=temp_message

######################################################################

st.title("How can I assist you today?")

# Loading the Conversation History
for message in st.session_state['message_history']:
    with st.chat_message(message['role']):
        st.text(message['content'])

user_input = st.chat_input('Type Here')

if user_input:

    # Detect first message in this conversation
    if len(st.session_state['message_history']) == 0:
        # Generate title using LLM
        generated_title = generate_title_from_llm(user_input)

        # Update chat_list entry
        for chat_data in st.session_state['chat_list']:
            if chat_data["id"] == st.session_state['thread_id']:
                chat_data["title"] = generated_title

    st.session_state['message_history'].append({'role':'user','content':user_input})

    with st.chat_message('user'):
        st.text(user_input)

    def stream_response():
        for message_chunk, metadata in workflow.stream(
            {"messages":[HumanMessage(content=user_input)]},
            config={'configurable':{'thread_id':st.session_state['thread_id']}},
            stream_mode='messages'
        ):
           
            yield message_chunk.content

    with st.chat_message('assistant'):
        ai_message = st.write_stream(stream_response())

    st.session_state['message_history'].append({'role':'assistant','content':ai_message})