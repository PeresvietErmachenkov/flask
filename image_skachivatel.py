from PIL import Image
import io
import requests

responce = requests.get("https://hniesfp.imgix.net/8/images/detailed/683/Mobile_Google_Pixel_GA04915-GB.jpg?fit=fill&bg=0FFF&w=1500&h=1000&auto=format,compress")
saving_image = Image.open(io.BytesIO(responce.content))
saving_image.save("static/images/8pro.png")

