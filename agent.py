from langchain.agents import create_agent
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.agents.middleware import SummarizationMiddleware
from langgraph.checkpoint.memory import InMemorySaver
from dotenv import load_dotenv
import os
from rag import query_index
from search import web_search
load_dotenv()
api = os.getenv("GEMINI_API_KEY")

llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash", google_api_key=api)

checkpointer = InMemorySaver()

agent = create_agent(model=llm, tools=[web_search, query_index], middleware=[SummarizationMiddleware(model=ChatGoogleGenerativeAI(model="gemini-2.0-flash-lite", google_api_key=api), max_tokens_before_summary=1000, messages_to_keep=10)], checkpointer=checkpointer, system_prompt="You are an AI assistant that shall provide the demanded information by trying your level best. You have memory, access to the internet, and access to the documents uploaded by the user.")

