from pydantic import BaseModel
from typing import Dict, Any, List

class GraphDefinition(BaseModel):
    nodes: List[str]
    edges: Dict[str, str]
    start_node: str

class RunRequest(BaseModel):
    graph_id: str
    initial_state: Dict[str, Any]

class RunResult(BaseModel):
    final_state: Dict[str, Any]
    log: List[str]
