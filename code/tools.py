import logging
from langchain.tools import tool
from langchain_tavily import TavilySearch

logger = logging.getLogger(__name__)

tavily_search=TavilySearch(
    max_results=1,
    topic="general",
)

@tool
def Tavily_tools(query: str) -> str:
    """当需要根据现有的食材来选择食谱时，调用该工具搜索食谱"""
    logger.info("Tavily is calling")
    return tavily_search.invoke(query) 