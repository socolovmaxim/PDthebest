import os
import shutil

# Укажите путь к датасету и путь для сохранения файлов
dataset_directory = '/путь/к/датасету'
output_directory = '/путь/для/сохранения'

for root, dirs, files in os.walk(dataset_directory):
    for file in files:
        class_name = os.path.basename(root)
        new_filename = f"{class_name}_{file}"
        source_path = os.path.join(root, file)
        destination_path = os.path.join(output_directory, new_filename)
        shutil.copy(source_path, destination_path)
