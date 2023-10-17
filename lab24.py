import os
import requests
from bs4 import BeautifulSoup
import urllib.parse

# Функция для создания папки, если она не существует
def create_directory(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)

# Функция для загрузки изображений

def download_images(search_query, output_directory, num_pages):
    create_directory(output_directory)
    base_url = "https://www.google.com/search" + '?q=' +search_query + '&tbm=isch'
    print(base_url)
 
    for i in range(num_pages):

        img_tags = []
        response = requests.get(base_url)
        # print(response.url)
        soup = BeautifulSoup(response.text, 'html.parser')
        print(soup)
        img_tags = soup.find_all("img", {"class": "DS1iW"}) 
        print(img_tags)
       
        

        for img_tag in img_tags:
          
            img_url = img_tag["src"]
            img_url = urllib.parse.urljoin(base_url, img_url)
            # print(img_url)
            img_data = requests.get(img_url).content
        

            # Создаем имя файла в формате 0000.jpg, 0001.jpg и т.д.
            filename = f"{i * len(img_tags) + img_tags.index(img_tag):04d}.jpg"
            file_path = os.path.join(output_directory, filename)

            # Записываем изображение в файл
            with open(file_path, 'wb') as img_file:
                img_file.write(img_data)


# Загрузка изображений роз
download_images('rose', 'dataset/rose', 1)
# Загрузка изображений тюльпанов
download_images('tulip', 'dataset/tulip', 1)
