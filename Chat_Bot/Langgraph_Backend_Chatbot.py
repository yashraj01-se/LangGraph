from langgraph.graph import StateGraph, START , END
from typing import TypedDict, Annotated , List
from pydantic import BaseModel , Field
from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage , BaseMessage
import os
import operator
from langgraph.graph.message import add_messages
from langgraph.checkpoint.memory import MemorySaver
import asyncio

from dotenv import load_dotenv
load_dotenv()

os.environ["PYTORCH_JIT"] = "0"

# Compatible with Streamlit & python 3.10+
try:
    loop = asyncio.get_event_loop()
except RuntimeError:
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)

if loop.is_closed():
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)

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

check_pointer = MemorySaver()
graph = StateGraph(state_schema=ChatState)

graph.add_node("llm_chat", llm_chat)
graph.add_edge(START, "llm_chat")
graph.add_edge("llm_chat", END)


graph.set_entry_point("llm_chat")  

workflow = graph.compile(checkpointer=check_pointer)
