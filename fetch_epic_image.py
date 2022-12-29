import requests
from getimageslib import get_image, get_nasa_api_key
from datetime import datetime


def main():    

    try:
        fetch_epic()
    except requests.exceptions.HTTPError:
        print('Неверная ссылка на загрузку фотографий или неверный api_key')


def fetch_epic():

    url_params = {
            'api_key': get_nasa_api_key()}
             
    url = 'https://api.nasa.gov/EPIC/api/natural/images'
    response = requests.get(url, params=url_params)
    response.raise_for_status()    
    response = response.json()        
    images_date = datetime.fromisoformat(response[0]['date'])
    images_date = images_date.strftime('%Y/%m/%d') 
    image_dir = 'epic_image'                
    for link_number, image in enumerate(response):
        link = image['image']   
        url = f'https://api.nasa.gov/EPIC/archive/natural/{images_date}/png/{link}.png'
        image_file = f'epic_{link_number}.png'
        get_image(url, image_file, image_dir, url_params)


if __name__ == "__main__":
    
    main()