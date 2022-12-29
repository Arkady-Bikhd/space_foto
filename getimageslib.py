import requests
from pathlib import Path
from urllib.parse import urlparse
from dotenv import load_dotenv
from os import environ


def main():
    pass
    

def get_telegram_token():
    load_dotenv()
    return environ['TELEGRAM_TOKEN']


def get_tg_chat_id():
    load_dotenv()
    return environ['TG_CHAT_ID']


def get_nasa_api_key():
    load_dotenv()
    return environ['NASA_API_KEY']


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

if "_name_" == '__main__':
    main()