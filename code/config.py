import os
from dotenv import load_dotenv
load_dotenv()
class ConfigQwen:
    def __init__(self):
        self.api_key = os.getenv("DASHSCORE_API_KEY")
        self.base_url = "https://dashscope.aliyuncs.com/compatible-mode/v1"
        self.model_name = "qwen3.7-plus"
class Config:
    def __init__(self):
        self.qwen = ConfigQwen()
