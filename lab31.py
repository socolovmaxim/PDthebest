#1.	Написать скрипт для формирования текстового файла-аннотации собранного датасета. 
#Файл-аннотация должен представлять собой csv-файл, в котором в первой колонке будет 
#указан абсолютный путь к файлу, во второй колонке относительный путь относительно 
#вашего Python-проекта, третья колонка будет содержать текстовое название класса (метку класса), к которому относится данный экземпляр.

import os
import csv

# Укажите директории, где находятся собранные изображения
rose_directory = 'dataset/rose'
tulip_directory = 'dataset/tulip'

# Создайте функцию для создания аннотаций
def create_annotation_csv(image_directory, class_label):
    annotation = []
    for root, _, files in os.walk(image_directory):
        for file in files:
            absolute_path = os.path.join(root, file)
            relative_path = os.path.relpath(absolute_path, start=os.getcwd())
            annotation.append([absolute_path, relative_path, class_label])

    return annotation

# Создайте аннотации для роз
rose_annotation = create_annotation_csv(rose_directory, 'rose')

# Создайте аннотации для тюльпанов
tulip_annotation = create_annotation_csv(tulip_directory, 'tulip')

# Объедините аннотации для всех классов
annotations = rose_annotation + tulip_annotation

# Укажите путь к файлу CSV для сохранения аннотаций
csv_file = 'dataset_annotations.csv'

# Запишите аннотации в CSV-файл
with open(csv_file, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Absolute Path', 'Relative Path', 'Class Label'])
    for row in annotations:
        writer.writerow(row)

print(f"Аннотации сохранены в файле {csv_file}")


