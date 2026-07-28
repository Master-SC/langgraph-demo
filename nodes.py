from dotenv import load_dotenv
from langchain.tools import tool_node
from langgraph.graph import MessagesState
from langgraph.prebuilt import ToolNode

from react import llm,tools

load_dotenv()

SYSTEM_MESSAGE="""
You are a helpful assistance that has tools calling capability to answer questions.
"""

def run_agent_reasoning(state: MessagesState) -> MessagesState:
    """
    Run the Agent Reasoning Node.
    """
    response = llm.invoke([{"role":"system","content":SYSTEM_MESSAGE}, *state["messages"]])
    return {"messages":[response]}

tool_node = ToolNode(tools)

