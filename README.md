# Bing Image Search Downloader

This Python script uses the Bing Image Search API to download images based on a search query.

## Requirements

- Python 3
- `requests` library
- `PIL` library

## Usage
Before running the script, you need to enter your Bing Image Search API key in the `search_bing_api.py` file. Replace the `API_KEY` variable with your own API key:

```python
API_KEY = "your_api_key_here"
```
[Go to getting the API Key section](#getting-the-bing-image-search-api-key)

You can run the script from the command line with the following arguments:

- `-q` or `--query`: The search query for the Bing Image Search API. This argument is required.
- `-c` or `--count`: The number of images to download. The default is 50.
- `-d` or `--directory`: The directory to save the images. The default is './images'.
- `-l` or `--license`: The license type for the images. The default is 'public'. Other possible values are 'All', 'Any', 'Share', 'ShareCommercially', 'Modify', 'ModifyCommercially'.
- `-o` or `--offset`: The offset to start the search from. The default is 0.

Here's an example of how to run the script:

```bash
python search_bing_api.py -q "cats" -c 100 -d "./cat_images" -l "public" -o 0
```

This will download 100 public images of cats to the 'cat_images' directory, starting from the first image in the search results.

## Getting the Bing Image Search API Key

To use this script, you'll need a Bing Image Search API key. Here are the steps to obtain it:

1. Go to the Bing Image Search API Page(https://www.microsoft.com/en-us/bing/apis/bing-image-search-api).
2. Click on "Create a resource".
3. In the "Search the Marketplace" box, search for "Bing Search v7".
4. In the search results, click on "Bing Search v7" and then click "Create".
5. Fill in the form with the necessary information and click "Review + create", then "Create" on the next page.
6. Once the resource is created, go to the "Keys and Endpoint" section.
7. Copy one of the keys. This is the API key you'll use in the script.

After obtaining the API key, replace the `API_KEY` variable in the `search_bing_api.py` file with your own API key:

```python
API_KEY = "your_api_key_here"
```
Steps to get your API key:
## Getting the Bing Image Search API Key

To use this script, you'll need a Bing Image Search API key. Here are the steps to obtain it:

1. Go to the [Azure portal](https://portal.azure.com/).
2. Click on "Create a resource".
3. In the "Search the Marketplace" box, search for "Bing Search v7".
4. In the search results, click on "Bing Search v7" and then click "Create".
5. Fill in the form with the necessary information and click "Review + create", then "Create" on the next page.
6. Once the resource is created, go to the "Keys and Endpoint" section.
7. Copy one of the keys. This is the API key you'll use in the script.

After obtaining the API key, replace the `API_KEY` variable in the `search_bing_api.py` file with your own API key:

```python
API_KEY = "your_api_key_here"
```
