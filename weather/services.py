import random
import requests

from bs4 import BeautifulSoup
import fake_useragent


def get_city_image_url(city: str) -> str:

    user = fake_useragent.UserAgent().random
    header = {
        'user-agent': user,
    }
    URL = 'https://yandex.ru/images/search?text='

    response = requests.get(f'{URL}{city}', headers=header)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'lxml')

        try:
            images = soup.find_all(
                'img', {'class': 'serp-item__thumb justifier__thumb'})
        except:
            image_url = None
        else:
            image_url = None
            # image = random.choice(images)
            # image_url = f"https:{image['src']}"

    return image_url


if __name__ == '__main__':
    get_city_image_url('Екатеринбург')
