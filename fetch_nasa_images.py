import requests
from random import randint
from getimageslib import get_image, fetch_file_extension
from dotenv import load_dotenv
from os import environ


def main():

    load_dotenv()
    try:           
        fetch_nasa_apod()        
    except requests.exceptions.HTTPError:
        print('Неверная ссылка загрузку фотографий или неправильный api_key')


def fetch_nasa_apod():

    images_count = randint(30, 51)
    nasa_api_key = environ['NASA_API_KEY']
    url_params = {
            'api_key': nasa_api_key,
            'count': images_count
        }
    url = 'https://api.nasa.gov/planetary/apod'
    response = requests.get(url, params=url_params)
    response.raise_for_status()    
    response = response.json() 
    image_dir = 'nasa_images'
    for link_number, link in enumerate(response):
        if link['media_type'] == 'image':
            image_link = link['hdurl']
        file_extension = fetch_file_extension(image_link)
        image_file = f'nasa{link_number}.{file_extension}'        
        get_image(image_link, image_file, image_dir)


if __name__ == "__main__":
    
    main()
