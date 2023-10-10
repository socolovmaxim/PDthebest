import os
import requests
from PIL import Image
import time

# Создаем папку "dataset", если она не существует
if not os.path.exists("dataset"):
    os.mkdir("dataset")

# Функция для загрузки изображений
def download_images(search_query, target_folder, num_images):
    base_url = "https://yandex.ru/images/search"
    params = {
        "text": search_query,
        "type": "photo",
    }

    # Создаем папку для класса
    if not os.path.exists(target_folder):
        os.mkdir(target_folder)

    for i in range(num_images):
        params["p"] = i + 1
        response = requests.get(base_url, params=params)

        if response.status_code == 200:
            # Ищем URL изображения в HTML-коде страницы
            image_url = response.text.split('class="serp-item__link i-bem" href="')[1].split('"')[0]
            image_response = requests.get(image_url)

            if image_response.status_code == 200:
                with open(f"{target_folder}/{str(i).zfill(4)}.jpg", "wb") as f:
                    f.write(image_response.content)

                # Добавляем задержку, чтобы избежать блокировки
                time.sleep(1)
            else:
                print(f"Ошибка при загрузке изображения {i + 1}")
        else:
            print(f"Ошибка при поиске изображения {i + 1}")

# Загрузка изображений роз
download_images('rose', 'dataset/rose', 1000)
# Загрузка изображений тюльпанов
download_images('tulip', 'dataset/tulip', 1000)