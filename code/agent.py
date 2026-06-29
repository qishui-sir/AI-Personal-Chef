from model import LLMEntity
from tools import Tavily_tools
from langchain.agents import create_agent
class Agent:
    def __init__(self):
        self.tools=[Tavily_tools]
        self.system_prompt="""
        
        """
    def qwen(self) -> str:
        return create_agent(
            model=LLMEntity.get_qwen(),
            tools=self.tools,
            system_prompt=self.system_prompt,
        )
