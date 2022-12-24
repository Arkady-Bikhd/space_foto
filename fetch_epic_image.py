import requests
from getimageslib import get_image
from dotenv import load_dotenv
from os import getenv


def main():    

            
    try:    
        fetch_epic()
    except requests.exceptions.HTTPError:
        print('Неверная ссылка на загрузку фотографий или неверный api_key')


def fetch_epic():

    load_dotenv()
    api_key_nasa = getenv('API_KEY_NASA')
    url_params = {
            'api_key': api_key_nasa}
    
    def get_epic_links(url_params):
        
        url = 'https://api.nasa.gov/EPIC/api/natural/images'
        response = requests.get(url, params=url_params)
        response.raise_for_status()
        epic_links = list()
        images_date = response.json()[0]['date']
        images_date = images_date.split(' ')[0]
        images_date = images_date.replace('-', '/')
        for link_number in range(len(response.json())):
            epic_links.append(response.json()[link_number]['image'])
        return images_date, epic_links

    image_date, image_links = get_epic_links(url_params)
    dir = 'epic_image'
    for link_number, link in enumerate(image_links):
        url = f'https://api.nasa.gov/EPIC/archive/natural/{image_date}/png/{link}.png'
        image_file = f'epic_{link_number}.png'
        get_image(url, image_file, dir, url_params)


if __name__ == "__main__":
    
    main()