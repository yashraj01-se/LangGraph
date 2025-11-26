---

# Agentic AI & LangGraph Learning Journey

A structured progression through modern agent systems, inspired by the CampusX LangGraph course.

---

## 📌 Overview

This repository documents a hands-on exploration of **Agentic AI**, **LangGraph**, and the system-level architecture behind modern AI workflows. The focus is on understanding how reliable, stateful, event-driven agents are engineered — not just running tutorials, but grasping how production-grade patterns fit together.

---

## ✅ Learning Roadmap

This repository follows the lecture flow and expands on the concepts introduced along the way.

---

### **Lecture 1 – Introduction to Generative AI vs Agentic AI**

* Why static prompt→response systems fall short
* Goals, tools, memory, and decisions
* Where agentic systems outperform plain LLM calls

---

### **Lecture 2 – What is Agentic AI?**

* Agents as autonomous, goal-directed systems
* Tool use, memory, feedback loops
* How LangGraph structures agent behaviour

---

### **Lecture 3 – Workflows vs Agents**

* Workflows = fixed paths
* Agents = adaptive, dynamic control flows
* LangChain limitations
* Event-driven design
* Retry, recovery, checkpointing
* Subgraphs and modular architecture

---

### **Lecture 4 – LangGraph Core Concepts**

* Nodes, edges, and directed execution
* StateGraph vs MessageGraph
* Mutation rules and state integrity
* Checkpointing + resumability
* Human-in-the-loop pauses
* The mental model of graph-based systems

---

### **Lecture 5 – Sequential Workflows**

* Linear deterministic flows
* Stepwise state updates
* Multi-step LLM pipelines
* Prompt-chaining using LangGraph
* Designing predictable, structured systems

---

### **Lecture 6 – Parallel Graph Execution & Structured Evaluation**

* Running multiple evaluator nodes in parallel
* Structured LLM output using Pydantic + LangGraph
* Reducers (`operator.add`) for merging state
* Computing aggregate scores and multi-criteria feedback
* Building a multi-phase UPSC essay evaluator

---

### **Lecture 7–9 – Conditional & Iterative Workflows**

* Conditional routing with decision nodes
* Branching execution paths
* Iterative refinement and repeated LLM loops
* Real-life examples of dynamic decision flows
* Using state to guide the next step

---

### **Lecture 10 – Building a Basic LLM Chatbot + Introducing Memory**

* Constructing a simple ChatBot inside LangGraph
* Understanding how **memory** is integrated into agent workflows
* Two approaches to memory:

  * **In-memory (RAM)** for short-lived sessions
  * **Persistent storage** (DB / local disk) for long-lived conversational agents
* How checkpointers store interaction history and enable continuity
* The fundamentals of conversational state management using LangGraph

---

### **Lecture 11 – Persistence & Long-Term Memory**

*Enabling long-lived agent sessions
*Using SQLite-based checkpointers, file checkpointers
*Storing and restoring entire graph state
*Session IDs & thread-based memory
*How persistence powers production chatbots

---

### **Lecture 12 – UI Development with Streamlit**

*Building a front-end for LangGraph agents
*Integrating workflow execution with Streamlit
*Real-time interaction, chat UI design
8Passing session state from UI → Graph
8Deploying lightweight agent-based applications

---

### **Lecture 13 – Streaming Responses in ChatBots**

*Token-by-token streaming from LLMs
*Real-time rendering in Streamlit
*Mixing streaming with persistent memory
*Improving UX through incremental output
*Designing responsive conversational agents

---

## 🧠 Why This Matters

Agentic AI powers many emerging real-world applications:

* automation engines
* research assistants
* tool-using systems
* voice/multimodal agents
* multi-agent orchestration

Understanding these patterns enables designing systems that are:

✅ reliable
✅ stateful
✅ fault-tolerant
✅ extendable
✅ production-ready

---

## 🤝 Connect

This repository is an ongoing log of the journey — experiments, insights, and incremental progress.
If you're working on **agentic systems, LangGraph, or AI infrastructure**, feel free to reach out or exchange ideas.

---
