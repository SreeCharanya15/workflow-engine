from typing import Callable, Dict, Any, List

GRAPHS: Dict[str, Dict[str, Any]] = {}
RUNS: Dict[str, Dict[str, Any]] = {}

NODES: Dict[str, Callable[[Dict[str, Any]], Dict[str, Any]]] = {}

def register_node(name: str):
    def decorator(func: Callable[[Dict[str, Any]], Dict[str, Any]]):
        NODES[name] = func
        return func
    return decorator

def create_graph(graph_id: str, nodes, edges, start_node: str):
    GRAPHS[graph_id] = {
        "nodes": nodes,
        "edges": edges,
        "start_node": start_node,
    }
    return graph_id

def run_graph(graph_id: str, initial_state: Dict[str, Any]):
    graph = GRAPHS[graph_id]
    current_node = graph["start_node"]
    state = initial_state.copy()
    log: List[str] = []

    while current_node is not None:
        log.append(f"Running node: {current_node}")
        node_func = NODES[current_node]
        state = node_func(state)

        if "next_node" in state:
            current_node = state.pop("next_node")
        else:
            current_node = graph["edges"].get(current_node)

    return state, log
