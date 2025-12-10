# Workflow Engine using FastAPI (Code Review Example)

This project implements a simple workflow engine using FastAPI. 
A graph of nodes is executed in sequence, passing a shared "state" 
object between nodes. Supports branching, looping, and logging.


![Python](https://img.shields.io/badge/python-3.11-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-framework-green)
  

# Why I built this 
This project was built as part of a workflow assignment to show how backend workflows can be executed dynamically through APIs.

# Features
- Node based architecture
- Sequential execution
- Graph definition using JSON
- Shared state
- Branching via next_node
- Looping (until quality threshold achieved)
- Logging of node execution
- In-memory run history

# Tech Stack
Python 3.11, FastAPI, Uvicorn

# API Endpoints
POST /graph/create
POST /graph/run
GET /graph/state/{run_id}

# Example Usage
-Create graph
{
  "nodes": [
    "extract_functions",
    "check_complexity",
    "detect_issues",
    "suggest_improvements"
  ],
  "edges": {
    "extract_functions": "check_complexity",
    "check_complexity": "detect_issues",
    "detect_issues": "suggest_improvements"
  },
  "start_node": "extract_functions"
}

- Run Workflow
{
  "graph_id": "graph_1",
  "initial_state": {
    "code": "def add(a, b): return a + b\n\ndef mul(a, b): return a * b",
    "threshold": 70
  }
}



# How to run locally
- git clone https://github.com/SreeCharanya15/workflow-engine
- cd tredence-workflow-engine
- python -m venv venv
- venv\Scripts\activate
- pip install -r requirements.txt
- uvicorn app.main:app --reload

# Future Improvements
- Database storage
- Authentication
- GUI Workflow builder
- Multi-branch graph support
- Advanced AI code analysis




