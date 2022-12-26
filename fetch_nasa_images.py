import requests
from random import randint
from getimageslib import get_image, fetch_file_extension
from dotenv import load_dotenv
from os import environ


def main():

    load_dotenv()
    global nasa_api_key
    nasa_api_key = environ['NASA_API_KEY']    
    try:           
        fetch_nasa_apod()        
    except requests.exceptions.HTTPError:
        print('Неверная ссылка загрузку фотографий или неправильный api_key')


def fetch_nasa_apod():

    def get_nasa_apod_links(images_count):
        
        url_params = {
            'api_key': nasa_api_key,
            'count': images_count
        }
        url = 'https://api.nasa.gov/planetary/apod'
        response = requests.get(url, params=url_params)
        response.raise_for_status()
        apod_links = list()
        for link_number in range(len(response.json())):
            apod_links.append(response.json()[link_number]['hdurl'])
            
        return apod_links

    images_count = randint(30, 51)    
    images_links = get_nasa_apod_links(images_count)
    image_dir = 'nasa_images'
    for link_number, link in enumerate(images_links):
        file_extension = fetch_file_extension(link)
        image_file = f'nasa{link_number}.{file_extension}'        
        get_image(link, image_file, image_dir)


if __name__ == "__main__":
    
    main()
