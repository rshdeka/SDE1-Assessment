import pandas as pd
import requests
from PIL import Image
from io import BytesIO
import uuid

def compress_image(input_url):
    response = requests.get(input_url)
    img = Image.open(BytesIO(response.content))
    output_buffer = BytesIO()
    img.save(output_buffer, format='JPEG', quality=50)
    output_url = "https://storage.example.com/" + str(uuid.uuid4()) + ".jpg"
    return output_url

def process_csv(csv_file_path, request_id):
    df = pd.read_csv(csv_file_path)
    df["Output Image Urls"] = df["Input Image Urls"].apply(
        lambda urls: ", ".join([compress_image(url.strip()) for url in urls.split(",")])
    )
    output_csv_path = f"output_{request_id}.csv"
    df.to_csv(output_csv_path, index=False)
    return output_csv_path