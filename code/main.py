from image import Image
from agent import Agent
from langchain.messages import HumanMessage
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
)

image_path = r"E:\Agent\AI-Personal-Chef\images\food.jpg"

if __name__ == "__main__":
    messages = HumanMessage(content=[
        {"type":"text","text":"请帮我根据图片的食材推荐一份食谱"},
        {"type":"image","base64":Image.encode_image(image_path),"mime_type":"image/jpeg"}
    ])
    agent = Agent()
    agent_qwen = agent.qwen()
    response = agent_qwen.invoke(
        {"messages":[messages]}
    )
    print(response["messages"][-1].content)