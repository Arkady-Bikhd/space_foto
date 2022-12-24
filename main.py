import requests
from pathlib import Path
from urllib.parse import urlparse
from random import randint


def main():
    
    url = 'https://example.com/txt/hello%20world.txt?v=9#python'
    
    try:    
        #fetch_spacex_last_launch()
        #fetch_nasa_apod()
        fetch_epic()
    except requests.exceptions.HTTPError:
        print('Неверная ссылка на запуск SpaceX')
    #print(fetch_file_extension(url))


def get_image(url, image_file, dir, url_params=''):

    response = requests.get(url, params=url_params)
    response.raise_for_status()
    current_dir = Path.cwd() 
    Path(f'{current_dir}\{dir}').mkdir(parents=True, exist_ok=True)
    file_name = Path() / current_dir / dir / image_file
    with open(file_name, 'wb') as file:
        file.write(response.content)


def get_spacex_launch_links(id):

    url = f'https://api.spacexdata.com/v3/launches/{id}'
    response = requests.get(url)
    response.raise_for_status()
    return response.json()['links']['flickr_images']


def fetch_spacex_last_launch():
    
    images_links = get_spacex_launch_links(66)
    dir = 'images'
    for link_number, link in enumerate(images_links):
        image_file = f'spacex{link_number}.jpg'        
        get_image(link, image_file, dir)


def fetch_file_extension(url):

    parced_link = urlparse(url)    
    return Path(parced_link.path).suffix
    

def fetch_nasa_apod():

    def get_nasa_apod_links(count_images):
        
        url_params = {
            'api_key': 'z0lvPbvoXdFG0ofUnWbmTHR0r1Xchf3cA7IYIBEi',
            'count': count_images
        }
        url = 'https://api.nasa.gov/planetary/apod'
        response = requests.get(url, params=url_params)
        response.raise_for_status()
        apod_links = list()
        for link_number in range(len(response.json())):
            apod_links.append(response.json()[link_number]['hdurl'])
            
        return apod_links

    count_images = randint(30, 51)    
    images_links = get_nasa_apod_links(count_images)
    dir = 'nasa_images'
    for link_number, link in enumerate(images_links):
        file_extension = fetch_file_extension(link)
        image_file = f'nasa{link_number}.{file_extension}'        
        get_image(link, image_file, dir)


def fetch_epic():

    url_params = {
            'api_key': 'z0lvPbvoXdFG0ofUnWbmTHR0r1Xchf3cA7IYIBEi'}
    
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