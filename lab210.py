import os
import requests
from bs4 import BeautifulSoup

# URL страницы с отзывами
url = "https://www.livelib.ru/reviews/~2#reviews"

# Количество отзывов для каждой оценки (звезд)
num_reviews_per_rating = 1000
num_ratings = 5  # От 1 до 5 звезд

# Папка для сохранения отзывов
output_folder = "dataset"

# Создаем папку output_folder, если её нет
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Определите функцию для получения отзывов с заданной страницы
def get_reviews(page_url):
    response = requests.get(page_url)
    soup = BeautifulSoup(response.text, "html.parser")

    # Найдем отзывы на странице (вы можете анализировать HTML для конкретного сайта)
    reviews = soup.find_all("div", class_="b-review-full-text")  # Это может потребовать анализа HTML сайта

    return reviews

# Определите функцию для сохранения отзыва в файл
def save_review_to_file(rating, review_number, book_name, review_text):
    folder_path = os.path.join(output_folder, str(rating))
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    
    filename = f"{review_number:04d}.txt"  # Дополняем номер файла нулями
    file_path = os.path.join(folder_path, filename)
    
    with open(file_path, "w", encoding="utf-8") as file:
        file.write(f"Book Name: {book_name}\n")
        file.write(review_text)

# Перебираем оценки (звезды)
for rating in range(1, num_ratings + 1):
    for review_number in range(num_reviews_per_rating):
        page_url = f"{url}?p={review_number + 1}&rating={rating}"

        reviews = get_reviews(page_url)

        # Сохраняем каждый отзыв в отдельный файл
        for review in reviews:
            book_name = "Book Name"  # Вы можете извлекать имя книги из страницы
            review_text = review.get_text()
            save_review_to_file(rating, review_number, book_name, review_text)
