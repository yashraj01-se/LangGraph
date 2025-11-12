---
# Agentic AI & LangGraph Learning Journey

*A structured progression through modern agent systems, inspired by the CampusX LangGraph course.*
---

## 📌 Overview

This repository documents a hands-on exploration of **Agentic AI**, **LangGraph**, and the system-level architecture behind modern AI workflows. The focus is on understanding how reliable, stateful, event-driven agents are engineered — not just running tutorials, but grasping how production-grade patterns fit together.

---

## ✅ Learning Roadmap

This repository follows the lecture flow and expands on the concepts introduced along the way.

### **Lecture 1 – Introduction to Generative AI vs Agentic AI**

* Why static prompt→response systems fall short
* Goals, tools, memory, and decisions
* Where agentic systems outperform plain LLM calls

---

### **Lecture 2 – What is Agentic AI?**

* Agents as autonomous, goal-directed systems
* Tool use, memory, feedback loops
* How LangGraph brings structure to agent behavior

---

### **Lecture 3 – Workflows vs Agents**

* Workflows = fixed paths
* Agents = dynamic, adaptive control flows
* LangChain limitations
* Event-driven execution
* Retry, recovery, checkpointing
* Subgraphs and modular design

---

### **Lecture 4 – LangGraph Core Concepts**

* Nodes, edges, and directed execution
* StateGraph vs MessageGraph
* State mutation rules
* Checkpointing and resumability
* Human-in-the-loop pauses
* The mental model of graph-based agents

---

### **Lecture 5 – Sequential Workflows**

* Designing linear, deterministic flows
* Passing updated state step-by-step
* Multi-step LLM pipelines
* Prompt chaining using LangGraph
* Building structured, predictable logic

---

### **Lecture 6 – Parallel Graph Execution & Structured Evaluation**

* Implementing multiple evaluation nodes in parallel
* Defining structured schemas for LLM output (Pydantic + LangGraph)
* Combining results using reducers (`operator.add`)
* Computing aggregate scores and feedback
* Building a consistent, multi-phase UPSC essay evaluation workflow

---

## 🧠 Why This Matters

Agentic AI is a foundational layer behind emerging real-world applications such as:

* automation engines
* research assistants
* structured tool users
* voice and multimodal agents
* multi-agent orchestration

Understanding these architectural patterns enables building AI systems that are:

✅ reliable
✅ stateful
✅ fault-tolerant
✅ extendable
✅ production-ready

---

## 🤝 Connect

This repository is a running log of the exploration, experiments, and incremental progress.
If you're working on agentic systems, LangGraph, or AI infrastructure, feel free to connect or share your perspective.

---
