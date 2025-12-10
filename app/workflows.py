from typing import Dict, Any
from .engine import register_node


# Node 1: Extract function definitions from the code
@register_node("extract_functions")
def extract_functions(state: Dict[str, Any]) -> Dict[str, Any]:
    code = state.get("code", "")
    lines = code.splitlines()

    # Simple way to detect functions
    functions = [line for line in lines if line.strip().startswith("def ")]

    state["functions"] = functions
    return state


# Node 2: Calculate a simple complexity score
@register_node("check_complexity")
def check_complexity(state: Dict[str, Any]) -> Dict[str, Any]:
    functions = state.get("functions", [])

    # Very basic scoring: each function adds 10 points
    complexity_score = len(functions) * 10

    state["complexity_score"] = complexity_score
    return state


# Node 3: Detect issues based on complexity
@register_node("detect_issues")
def detect_issues(state: Dict[str, Any]) -> Dict[str, Any]:
    issues = []

    # Example rule
    if state.get("complexity_score", 0) > 20:
        issues.append("Code may be too complex.")

    state["issues"] = issues
    return state


# Node 4: Suggest improvements and loop until threshold
@register_node("suggest_improvements")
def suggest_improvements(state: Dict[str, Any]) -> Dict[str, Any]:
    suggestions = []

    if state.get("issues"):
        suggestions.append("Consider splitting large functions into smaller ones.")
    else:
        suggestions.append("Code looks simple and clean.")

    state["suggestions"] = suggestions

    # Initial score
    base_score = 50

    # If issues exist, lower quality score
    # Start with a score and improve each loop
    old_score = state.get("quality_score", 50)
    state["quality_score"] = old_score + 10

    # Read threshold (default = 70)
    threshold = state.get("threshold", 70)

    # ⭐ LOOP condition:
    # If quality score is below threshold, repeat same node
    if state["quality_score"] < threshold:
        state["next_node"] = "suggest_improvements"

    return state
