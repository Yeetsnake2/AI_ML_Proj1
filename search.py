from tavily import TavilyClient
from dotenv import load_dotenv
from langchain.tools import tool
import os
load_dotenv()

api_key = os.getenv("TAVILY_API_KEY")

tavily_client = TavilyClient(api_key=api_key)

@tool(description="A web search tool that can be used to answer questions about current events or to find specific information on the web.")
def web_search(query: str) -> str:
    response = tavily_client.search(query=query, )
    return_str = "\n".join([response['results'][i]['content'] for i in range(len(response['results']))])
    return f"Results for {query}:\n{return_str}"