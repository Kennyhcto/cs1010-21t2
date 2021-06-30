import requests
from PIL import Image
import io

if __name__ == "__main__":
    resp = requests.get('https://source.unsplash.com/random?rainbow+unicorn')
    Image.open(io.BytesIO(resp.content)).show()