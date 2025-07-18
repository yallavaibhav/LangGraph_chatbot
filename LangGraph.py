# Tools
from langchain_community.tools import ArxivQueryRun, WikipediaQueryRun
from langchain_community.utilities import ArxivAPIWrapper, WikipediaAPIWrapper
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_community.tools.tavily_search import TavilySearchResults


from typing_extensions import TypedDict
from langchain_core.messages import AnyMessage
from typing import Annotated
from langgraph.graph.message import add_messages

from IPython.display import Image, display
from langgraph.graph import StateGraph, START, END
from langgraph.prebuilt import ToolNode
from langgraph.prebuilt import tools_condition


# Adding Memory
from langgraph.checkpoint.memory import MemorySaver
memory = MemorySaver()


# Loading keys
import os
from dotenv import load_dotenv
load_dotenv()
os.environ["TAVILY_API_KEY"] = os.getenv("TAVILY_API_KEY")
os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_PROJECT"] = 'ReAct-Agent'

# Three tools arixv, wiki, and Tavily
api_wrapper_arxiv = ArxivAPIWrapper(top_k_results=2, doc_content_chars_max=500)
arxiv = ArxivQueryRun(api_wrapper=api_wrapper_arxiv, description="Query arxiv papers")
api_wrapper_wiki = WikipediaAPIWrapper(top_k_results=1, doc_content_chars_max=500)
wiki = WikipediaQueryRun(api_wrapper=api_wrapper_wiki, description="Query the wiki")
tavily = TavilySearchResults()

## custom tools
def multiply(a:int, b:int)-> int:
    """ Multipy a and b
    Args: you will get two numbers
    """
    return a*b


#combine all the tools (bind)
tools = [wiki, arxiv, tavily, multiply]

# Initiilize my LLM
from langchain_groq import ChatGroq
llm = ChatGroq(model="qwen/qwen3-32b")
llm_bind_tools = llm.bind_tools(tools=tools)


class State(TypedDict):
    messages: Annotated[list[AnyMessage],add_messages]

## node creation
def llm_calling_tool(state:State):
    return {'messages': [llm_bind_tools.invoke(state['messages'])]}

## build graph
builder = StateGraph(State)
builder.add_node('llm_calling_tool',llm_calling_tool)
builder.add_node('tools', ToolNode(tools))

# Build Edges
builder.add_edge(START, 'llm_calling_tool')
builder.add_conditional_edges("llm_calling_tool", tools_condition) # either tools or end
builder.add_edge('tools', 'llm_calling_tool')

# graph  = builder.compile()
# display(Image(graph.get_graph().draw_mermaid_png()))
graph = builder.compile(checkpointer=memory)
config = {"configurable":{"thread_id":"1"}}
messages = graph.invoke({"messages": HumanMessage(content='Provide me the latest AI news')}, config = config)
for i in messages['messages']:
    i.pretty_print()

