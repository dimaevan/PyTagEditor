from PyQt6.QtCore import QSize
from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QApplication, QPushButton, QMainWindow, QFileDialog, QTableWidget, QLabel, QHeaderView
import sys
from work_with_files import get_list_of_files, check_tags
from pathlib import Path


def main():
    class MainWindow(QMainWindow):
        def __init__(self):
            super().__init__()

            self.setWindowTitle("Tag editor")
            self.setBaseSize(QSize(400, 400))
            self._createToolBars()
            self.create_table()

        def create_table(self, files: int = 1):
            table = QTableWidget(files, 9, self)
            self.setCentralWidget(table)
            table.setHorizontalHeaderLabels(
                ["Filename", "Artist", "Title", "Album", "Albumartist", "Date", "Genre", "Track number",
                 "Disk number"])

        def _createToolBars(self):
            action_bar = self.addToolBar("Toolbar")
            action_bar.setMovable(False)
            self.open_dir = QPushButton("")
            icon = "resources/open_folder_24.svg"
            icon_path = Path(icon)
            if icon_path.is_file():
                self.open_dir.setIcon(QIcon(icon))
            action_bar.addWidget(self.open_dir)
            self.open_dir.clicked.connect(self.open_directory)

        def open_directory(self):
            filepath = QFileDialog.getExistingDirectory(self, 'Select a directory with music')
            list_of_audio = get_list_of_files(filepath)
            # TODO Fix empty or invalid list
            if len(list_of_audio) != 0:
                check_tags(list_of_audio)

    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()


if __name__ == "__main__":
    main()
