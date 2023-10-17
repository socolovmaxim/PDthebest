#3.	Написать скрипт, создающий копию датасета таким образом, чтобы каждый файл из 
#сходного датасета получил случайный номер от 0 до 10000, и датасет представлял собой следующую структуру dataset/номер.jpg. 

import os
import random
import shutil

# Функция для создания папки, если она не существует
def create_directory(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)

# Функция для копирования и переименования файлов
def copy_and_rename_dataset(input_directory, output_directory):
    create_directory(output_directory)

    for root, _, files in os.walk(input_directory):
        for file in files:
            random_number = random.randint(0, 10000)
            new_filename = f"{random_number:04d}.jpg"
            source_path = os.path.join(root, file)
            destination_path = os.path.join(output_directory, new_filename)
            shutil.copy(source_path, destination_path)

# Укажите директории с исходным и целевым датасетами
input_directory = 'dataset'
output_directory = 'new_dataset'

# Копируйте и переименовывайте файлы
copy_and_rename_dataset(input_directory, output_directory)
