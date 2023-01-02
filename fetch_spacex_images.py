import requests
from getimageslib import get_image
import argparse

def main():
    
    spacex_id = create_parser_number()
    try:    
        fetch_spacex_launch(spacex_id)
    except requests.exceptions.HTTPError:
        print('Неверная ссылка на запуск SpaceX')
    

def get_spacex_launch_links(spacex_id):

    url = f'https://api.spacexdata.com/v3/launches/{spacex_id}'
    response = requests.get(url)    
    if response.ok:
        return response.json()['links']['flickr_images']    


def get_spacex_launch_links_latest():

    url = 'https://api.spacexdata.com/v5/launches/latest'
    response = requests.get(url)
    response.raise_for_status()
    return response.json()['links']['flickr']['original']        


def fetch_spacex_launch(spacex_id):
    
    images_links = None
    if spacex_id:
        images_links = get_spacex_launch_links(spacex_id)
    if not images_links and spacex_id:        
        print(f'Фотографий запуска с номером {spacex_id} не найдено.')
    else:
        print('Осуществляется поиск фотографий последнего запуска.')
        images_links = get_spacex_launch_links_latest()        
    if images_links:    
        image_dir = 'images'
        for link_number, link in enumerate(images_links):
            image_file = f'spacex{link_number}.jpg'        
            get_image(link, image_file, image_dir)
    elif not spacex_id:
        print('Фотографии не найдены')


def create_parser_number():

    parser = argparse.ArgumentParser(
        description='Программа скачивает фотографии запусков SpaceX'
    )
    parser.add_argument('-n', '--number', required=False, help='Введите номер запуска')
    args = parser.parse_args()

    return args.number


if __name__ == "__main__":
    
    main()