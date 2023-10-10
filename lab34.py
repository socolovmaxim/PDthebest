import os
import random

def get_next_instance(class_label, dataset_directory):
    instances = [f for f in os.listdir(dataset_directory) if os.path.isfile(os.path.join(dataset_directory, f)) and class_label in f]
    if instances:
        return os.path.join(dataset_directory, random.choice(instances))
    else:
        return None
