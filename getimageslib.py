import requests
from pathlib import Path
from urllib.parse import urlparse


def get_image(url, image_file, dir, url_params=''):

    response = requests.get(url, params=url_params)
    response.raise_for_status()
    current_dir = Path.cwd() 
    Path(f'{current_dir}\\{dir}').mkdir(parents=True, exist_ok=True)
    file_name = Path() / current_dir / dir / image_file
    with open(file_name, 'wb') as file:
        file.write(response.content)


def fetch_file_extension(url):

    parced_link = urlparse(url)    
    return Path(parced_link.path).suffix