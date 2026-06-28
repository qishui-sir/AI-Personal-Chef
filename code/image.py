import base64
class Image:
    def encode_image(path: str) -> str:
        """upload images to get file_id to analyse images"""
        with open(path,"rb") as image_file:
            image_data = image_file.read()
            base64_data = base64.b64encode(image_data)
            base64_messages = base64_data.decode("utf-8")
            return base64_messages