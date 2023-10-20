import os
import csv
import sys
from PyQt5 import QtWidgets, QtGui

class MainWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Dataset Annotation App")
        self.setGeometry(100, 100, 600, 400)

        self.folderpath = None
        self.dataset_annotations = []

        self.init_ui()

    def init_ui(self):
        layout = QtWidgets.QVBoxLayout()

        self.folderpath_label = QtWidgets.QLabel("Выберите папку с исходным датасетом:")
        self.folderpath_button = QtWidgets.QPushButton("Выбрать папку")
        self.folderpath_button.clicked.connect(self.get_dataset_folder)

        self.annotation_button = QtWidgets.QPushButton("Создать аннотацию")
        self.annotation_button.clicked.connect(self.create_annotations)

        self.next_image_button = QtWidgets.QPushButton("Следующая картинка")
        self.next_image_button.clicked.connect(self.show_next_image)
        self.image_label = QtWidgets.QLabel()
        self.current_image_index = 0

        layout.addWidget(self.folderpath_label)
        layout.addWidget(self.folderpath_button)
        layout.addWidget(self.annotation_button)
        layout.addWidget(self.next_image_button)
        layout.addWidget(self.image_label)

        self.setLayout(layout)

    def get_dataset_folder(self):
        self.folderpath = QtWidgets.QFileDialog.getExistingDirectory(self, 'Выберите папку с исходным датасетом')

    def create_annotations(self):
        if not self.folderpath:
            QtWidgets.QMessageBox.warning(self, "Внимание", "Выберите папку с исходным датасетом")
            return

        rose_directory = os.path.join(self.folderpath, 'rose')
        tulip_directory = os.path.join(self.folderpath, 'tulip')

        if not os.path.exists(rose_directory) or not os.path.exists(tulip_directory):
            QtWidgets.QMessageBox.warning(self, "Внимание", "Папки с изображениями не найдены")
            return

        rose_annotation = create_annotation_csv(rose_directory, 'rose')
        tulip_annotation = create_annotation_csv(tulip_directory, 'tulip')
        self.dataset_annotations = rose_annotation + tulip_annotation

        QtWidgets.QMessageBox.information(self, "Успех", "Аннотации созданы успешно")

    def show_next_image(self):
        if not self.dataset_annotations:
            QtWidgets.QMessageBox.warning(self, "Внимание", "Сначала создайте аннотации")
            return

        if self.current_image_index < len(self.dataset_annotations):
            image_path = self.dataset_annotations[self.current_image_index][0]
            pixmap = QtGui.QPixmap(image_path)
            self.image_label.setPixmap(pixmap)
            self.current_image_index += 1
        else:
            QtWidgets.QMessageBox.information(self, "Успех", "Все изображения просмотрены")

def create_annotation_csv(image_directory, class_label):
    annotation = []
    for root, _, files in os.walk(image_directory):
        for file in files:
            absolute_path = os.path.join(root, file)
            relative_path = os.path.relpath(absolute_path, start=os.getcwd())
            annotation.append([absolute_path, relative_path, class_label])
    return annotation

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
