import random

import requests
from bs4 import BeautifulSoup


def get_city_image_url(city: str) -> str:
    URL = 'https://yandex.ru/images/search?text='

    response = requests.get(f'{URL}{city}')
    soup = BeautifulSoup(response.text, 'lxml')

    images = soup.find_all(
        'img', {'class': 'serp-item__thumb justifier__thumb'})[:10]

    image = random.choice(images)

    image_url = f"https:{image['src']}"

    return image_url


if __name__ == '__main__':
    get_city_image_url('Екатеринбург')
