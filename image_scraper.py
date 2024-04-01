import os
import requests
from PIL import Image
from io import BytesIO
from datetime import datetime
import argparse
import hashlib
import json




# Enter your API key and endpoint URL here
API_KEY = "Paste Your Api Key Here"
URL = "https://api.bing.microsoft.com/v7.0/images/search"



# Define the search query
arg = argparse.ArgumentParser()
arg.add_argument("-q", "--query", required=True,
                help="Enter the search query for the Bing Image Search API")
arg.add_argument("-c", "--count", type=int, default=50 ,help="Enter the number of images to download default is 50")
arg.add_argument("-d", "--directory", default='./images' ,help="Enter the directory to save the images")
arg.add_argument("-l", "--license", default="public", help="Enter the license type for the images(All/Any/Public(DEFAULT)/Share/ShareComercially/Modify/ModifyComercially)")
arg.add_argument("-o", "--offset", default=0, help="Enter the offset to start the search from")
arg.add_argument("-m","--market", default="en-US", help="Enter the market to search from(https://learn.microsoft.com/en-us/bing/search-apis/bing-image-search/reference/market-codes)")
arg.add_argument("-ss", "--safe_search", default="Off", help="Enter the safe search level to use(Off/Moderate/Strict) ")
arg.add_argument("-s", "--size", default="All", help="Enter the size of the image to search for(Small/Medium/Large/All/Wallpaper)")
arg.add_argument("-a", "--aspect", default="All", help="Enter the aspect ratio of the image to search for(Squre/Wide/Tall/All) ")
arg.add_argument("-cl", "--color", default ="ColorOnly", help="Enter the color of the image to search for(ColorOnly/MonoChrome/Enter any dominant color) ")
args = vars(arg.parse_args())


# Get the arguments from the command line
query = args['query']
count = args['count']
final_directory = args['directory']
license = args['license']
offset = args['offset']
market = args['market']
safe_search = args['safe_search']
size = args['size']
aspect = args['aspect']
color = args['color']


# Creating a request to send to the API
headers = {"Ocp-Apim-Subscription-Key" : API_KEY}
params  = {"q": query, "count": count, "license": license, "imageType": "photo", offset: offset, "market": market, "safeSearch": safe_search, "size": size, "aspect": aspect, "color": color}
response = requests.get(URL, headers=headers, params=params)
response.raise_for_status()
search_results = response.json()
image_urls = [img['contentUrl'] for img in search_results["value"]]



# Load the image hashes from a file to avoid duplicates
try:
    with open('image_hashes.json', 'r') as f:
        image_hashes = set(json.load(f))
except FileNotFoundError:
    image_hashes = set()



# Download the images and save them to the specified directory
for i, url in enumerate(image_urls):
    try:
        image_data = requests.get(url)
        image_data.raise_for_status()
        image = Image.open(BytesIO(image_data.content))
        if image.mode == 'RGBA':
            image = image.convert('RGB')
            print("Converted RGBA image to RGB")


        # Calculate the hash of the image
        image_hash = hashlib.md5(image.tobytes()).hexdigest()
        if image_hash in image_hashes:
            print("Skipping duplicate image")
            continue
        image_hashes.add(image_hash)


        # Save the image to the specified directory default is images
        if not os.path.exists(final_directory):
            os.makedirs(final_directory)
        file_path = os.path.join(final_directory, f'{query}_{datetime.now().strftime('%Y%m%d%H%M%S')}{i}.jpg')
        with open(file_path, 'wb') as f:
            image.save(f, "JPEG")
        print(f"Downloaded {url} - saved to {file_path}")
    except Exception as e:
        print(f"Could not download {url} - {e}")



# Save the image hashes to a file to avoid duplicates in future
with open('image_hashes.json', 'w') as f:
    json.dump(list(image_hashes), f)      