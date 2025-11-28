from langgraph.graph import StateGraph, START , END
from typing import TypedDict, Annotated , List
from pydantic import BaseModel , Field
from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage , BaseMessage
import os
import operator
from langgraph.graph.message import add_messages
from langgraph.checkpoint.sqlite import SqliteSaver
import asyncio
import sqlite3

from dotenv import load_dotenv
load_dotenv()

os.environ["PYTORCH_JIT"] = "0"

model = ChatGroq(
    model="llama-3.1-8b-instant",
    api_key=os.getenv("GROQ_API_KEY")
)

class ChatState(TypedDict):
    messages: Annotated[List[BaseMessage], add_messages]

def llm_chat(state: ChatState):
    message = state['messages']
    response = model.invoke(message)
    return {'messages': response}


### Setting up SQLlite Checkpointers Connection :
conn=sqlite3.connect(database="chatbot.db",check_same_thread=False)
check_pointer = SqliteSaver(conn=conn)


graph = StateGraph(state_schema=ChatState)

graph.add_node("llm_chat", llm_chat)
graph.add_edge(START, "llm_chat")
graph.add_edge("llm_chat", END)


graph.set_entry_point("llm_chat")  

workflow = graph.compile(checkpointer=check_pointer)


def retreive_all_threads():
    all_thread=set()
    for checkpoint in check_pointer.list(None):
        all_thread.add(checkpoint.config['configurable']['thread_id'])

    return list(all_thread)
