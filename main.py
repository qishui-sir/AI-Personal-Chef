from langchain.chat_models import init_chat_model
from langchain_core.messages import HumanMessage
from langchain.tools import tool
from langchain.agents import create_agent
from openai import OpenAI
from dotenv import load_dotenv
import base64
import os
load_dotenv()

def upload_image(path: str) -> str:
    """upload images to get file_id to analyse images"""
    with open(image_path,"rb") as image_file:
        image_data = image_file.read()
        base64_data = base64.b64encode(image_data)
        base64_messages = base64_data.decode("utf-8")
        return base64_messages

image_path = r"E:\Agent\AI-Personal-Chef\images\kunkun.jpg"

human_messages = HumanMessage(content=[
    {"type":"text","text":"这张图片是什么意思"},
    {"type":"image","base64":upload_image(image_path),"mime_type":"image/jpeg",},
])

qwen_mod = init_chat_model(
    model = "qwen3.7-plus",
    model_provider="openai",
    api_key=os.getenv("DASHSCORE_API_KEY"),
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
)

response = qwen_mod.invoke([human_messages])

print(response)

