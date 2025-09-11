"""
graph.py

Defines the LangGraph workflow connecting Planner, Builder, and Critic agents.
"""
from langgraph.graph import StateGraph
from typing import Dict

# Import agent functions
from Agents.planner import run_planner
from Agents.builder import run_builder
from Agents.critic import run_critic


# --- Define state type ---
class AppState(Dict):
    """Shared state for LangGraph."""
    pass


# --- Build the workflow ---
def build_graph():
    graph = StateGraph(AppState)

    # Add nodes
    graph.add_node("planner", run_planner)
    graph.add_node("builder", run_builder)
    graph.add_node("critic", run_critic)

    # Add edges
    graph.add_edge("planner", "builder")
    graph.add_edge("builder", "critic")

    # Entry and terminal points
    graph.set_entry_point("planner")
    graph.set_finish_point("critic")

    return graph


if __name__ == "__main__":
    # Quick test run
    g = build_graph()
    app = g.compile()
    
    result = app({"prompt": "Build me a simple website with Flask backend and React frontend."})
    print("--- Final Graph Output ---")
    print(result)