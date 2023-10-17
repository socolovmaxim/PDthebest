#2.	Написать скрипт для копирования датасета в другую директорию таким образом, чтобы 
#имена файлов содержали имя класса и его порядковый номер. То есть из 
#dataset/class/0000.jpg должно получиться dataset/class_0000.jpg. Для того чтобы осталась 
#возможность определить принадлежность экземпляра к классу создать файл-аннотацию (как в пункте 1).

import os
import shutil
import csv

# Функция для копирования и переименования файлов с созданием аннотаций
def copy_and_rename_dataset(input_directory, output_directory, class_name):
    create_directory(output_directory)
    annotation = []

    for root, _, files in os.walk(input_directory):
        for index, file in enumerate(files):
            source_path = os.path.join(root, file)
            new_filename = f"{class_name}_{index:04d}.jpg"
            destination_path = os.path.join(output_directory, new_filename)
            shutil.copy(source_path, destination_path)
            annotation.append([destination_path, new_filename, class_name])

    return annotation

# Функция для создания папки, если она не существует
def create_directory(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)

# Создайте аннотации для роз
rose_annotations = copy_and_rename_dataset('dataset/rose', 'new_dataset/rose', 'rose')

# Создайте аннотации для тюльпанов
tulip_annotations = copy_and_rename_dataset('dataset/tulip', 'new_dataset/tulip', 'tulip')

# Объедините аннотации для всех классов
annotations = rose_annotations + tulip_annotations

# Укажите путь к файлу CSV для сохранения аннотаций
csv_file = 'dataset_annotations.csv'

# Запишите аннотации в CSV-файл
with open(csv_file, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Absolute Path', 'Relative Path', 'Class Label'])
    for row in annotations:
        writer.writerow(row)

print(f"Аннотации сохранены в файле {csv_file}")
