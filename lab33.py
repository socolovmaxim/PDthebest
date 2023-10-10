import os
import shutil
import random

# Укажите путь к датасету и путь для сохранения файлов
dataset_directory = '/путь/к/датасету'
output_directory = '/путь/для/сохранения'

if not os.path.exists(output_directory):
    os.makedirs(output_directory)

for root, dirs, files in os.walk(dataset_directory):
    for file in files:
        random_number = random.randint(0, 10000)
        new_filename = f"{random_number}.jpg"
        source_path = os.path.join(root, file)
        destination_path = os.path.join(output_directory, new_filename)
        shutil.copy(source_path, destination_path)
