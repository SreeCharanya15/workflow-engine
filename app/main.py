from fastapi import FastAPI
from .models import GraphDefinition, RunRequest
from .engine import create_graph, run_graph, RUNS
import app.workflows   # Ensures nodes are registered

app = FastAPI()


# 1) CREATE GRAPH
@app.post("/graph/create")
def create_graph_endpoint(defn: GraphDefinition):
    graph_id = "graph_1"
    create_graph(
        graph_id=graph_id,
        nodes=defn.nodes,
        edges=defn.edges,
        start_node=defn.start_node,
    )
    return {"graph_id": graph_id}


# 2) RUN GRAPH
@app.post("/graph/run")
def run_graph_endpoint(request: RunRequest):
    final_state, log = run_graph(request.graph_id, request.initial_state)
    run_id = f"run_{len(RUNS) + 1}"
    RUNS[run_id] = {
        "state": final_state,
        "log": log,
    }
    return {
        "run_id": run_id,
        "final_state": final_state,
        "log": log
    }


# 3) GET STATE
@app.get("/graph/state/{run_id}")
def get_state(run_id: str):
    run = RUNS.get(run_id)
    if not run:
        return {"error": "run_id not found"}
    return run
