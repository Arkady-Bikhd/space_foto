import requests
from pathlib import Path
from urllib.parse import urlparse
from dotenv import load_dotenv
from os import environ


load_dotenv()
telegram_token = environ['TELEGRAM_TOKEN']
tg_chat_id = environ['TG_CHAT_ID']
nasa_api_key = environ['NASA_API_KEY']


def get_image(url, image_file, image_dir, url_params=None):

    response = requests.get(url, params=url_params)
    response.raise_for_status()
    current_dir = Path.cwd() 
    Path(f'{current_dir}\\{image_dir}').mkdir(parents=True, exist_ok=True)
    file_name = Path() / current_dir / image_dir / image_file
    with open(file_name, 'wb') as file:
        file.write(response.content)


def fetch_file_extension(url):

    parsed_link = urlparse(url)    
    return Path(parsed_link.path).suffix