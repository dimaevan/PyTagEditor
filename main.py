from PyQt6.QtCore import QSize
from PyQt6.QtWidgets import QApplication, QPushButton, QMainWindow, QFileDialog
import sys
from work_with_files import get_list_of_files, check_tags


def main():
    class MainWindow(QMainWindow):
        def __init__(self):
            super().__init__()

            self.setWindowTitle("Tag editor")
            self.setFixedSize(QSize(400, 400))

            button = QPushButton("Open directory")
            button.clicked.connect(self.open_directory)
            self.setCentralWidget(button)

        def open_directory(self):
            filepath = QFileDialog.getExistingDirectory(self, 'Select a directory with music')
            list_of_audio = get_list_of_files(filepath)
            check_tags(list_of_audio)

    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()

    app.exec()


if __name__ == "__main__":
    main()
