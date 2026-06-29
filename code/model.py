from langchain_qwq.chat_models import ChatQwen
from config import Config

config = Config()
class LLMEntity:
    @staticmethod
    def get_qwen(): 
        return ChatQwen(
            model=config.qwen.model_name,
            api_key=config.qwen.api_key,
            base_url=config.qwen.base_url,
        )


