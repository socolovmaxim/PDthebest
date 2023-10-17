#4.	Написать скрипт, содержащий функцию, получающую на входе метку класса и 
#возвращающую следующий экземпляр (путь к нему) этого класса. Экземпляры идут в 
#любом порядке, но не повторяются. Когда экземпляры заканчиваются, функция возвращает None.

import os
import random

# Функция для получения следующего экземпляра класса
def get_next_instance(class_label, dataset_directory):
    class_directory = os.path.join(dataset_directory, class_label)

    if not os.path.exists(class_directory):
        return None

    files = [file for file in os.listdir(class_directory) if file.endswith('.jpg')]
    if not files:
        return None

    random.shuffle(files)
    next_instance = files.pop()
    file_path = os.path.join(class_directory, next_instance)

    return file_path

# Укажите путь к вашему датасету
dataset_directory = 'dataset'

# Пример использования функции
class_label = 'rose'
next_instance = get_next_instance(class_label, dataset_directory)

if next_instance is not None:
    print(f"Следующий экземпляр класса '{class_label}': {next_instance}")
else:
    print(f"Класс '{class_label}' закончился.")
