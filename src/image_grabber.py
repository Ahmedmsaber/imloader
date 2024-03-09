# src/image_grabber.py

import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse, urljoin

def download_image(url, output_folder, referer=None):
    headers = {"Referer": referer} if referer else {}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        # Extract the image name from the URL
        image_name = os.path.basename(urlparse(url).path)
        output_path = os.path.join(output_folder, image_name)

        # Save the image
        with open(output_path, 'wb') as f:
            f.write(response.content)

        print(f"Image downloaded: {image_name}")
    else:
        print(f"Failed to download image from {url}")

def grab_images_from_webpage(webpage_url, output_folder):
    response = requests.get(webpage_url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        img_tags = soup.find_all('img')

        for img_tag in img_tags:
            img_url = urljoin(webpage_url, img_tag['src'])
            download_image(img_url, output_folder, referer=webpage_url)
    else:
        print(f"Failed to fetch webpage: {webpage_url}")
