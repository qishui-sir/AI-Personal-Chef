from model import LLMEntity
from image import Image
from langchain.messages import HumanMessage

image_path = r"E:\Agent\AI-Personal-Chef\images\kunkun.jpg"

if __name__ == "__main__":
    llm_entity = LLMEntity()
    Qwen_mod = llm_entity.get_qwen()

    messages = HumanMessage(content=[
        {"type":"text","text":"这张图片是什么意思"},
        {"type":"image","base64":Image.encode_image(image_path),"mime_type":"image/jpeg"}
    ])
    response = Qwen_mod.invoke([messages])
    print(response)