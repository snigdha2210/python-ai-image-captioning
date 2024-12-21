import requests

from requests.exceptions import RequestException
from PIL import Image
from io import BytesIO
from bs4 import BeautifulSoup
from transformers import AutoProcessor, BlipForConditionalGeneration

def main():
    try:
        # Load the pretrained processor and model
        processor = AutoProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
        model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")
    except Exception as e:
        print(f"Error loading model: {e}")
        return

    # URL of the page to scrape
    url = "https://en.wikipedia.org/wiki/IBM"

    try:
        # Download the page
        response = requests.get(url)
        response.raise_for_status()
    except RequestException as e:
        print(f"Error fetching URL: {e}")
        return

    # Parse the page with BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')
    img_elements = soup.find_all('img')

    # Open a file to write the captions
    with open("captions.txt", "w") as caption_file:
        for img_element in img_elements:
            img_url = img_element.get('src')

            if not img_url or 'svg' in img_url or '1x1' in img_url:
                continue

            if img_url.startswith('//'):
                img_url = 'https:' + img_url
            elif not img_url.startswith('http'):
                continue

            try:
                # Download the image
                img_response = requests.get(img_url)
                img_response.raise_for_status()
                raw_image = Image.open(BytesIO(img_response.content))

                if raw_image.size[0] * raw_image.size[1] < 400:
                    continue

                raw_image = raw_image.convert('RGB')
                inputs = processor(raw_image, return_tensors="pt")
                out = model.generate(**inputs, max_new_tokens=50)
                caption = processor.decode(out[0], skip_special_tokens=True)

                caption_file.write(f"{img_url}: {caption}\n")
            except Exception as e:
                print(f"Error processing image {img_url}: {e}")
                continue

if __name__ == "__main__":
    main()
