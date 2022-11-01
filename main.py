from dataclasses import dataclass
from PyQt6.QtCore import QSize
from PyQt6.QtWidgets import QApplication, QPushButton, QMainWindow, QFileDialog
import taglib
from pathlib import Path
import sys

audio_dir = Path(__file__)
audio_files = []
audio_tags = {}


@dataclass
class Tag:
    Artist: str = ""
    Title: str = ""
    Album: str = ""
    Album_artist: str = ""
    Date: str = ""
    Genre: str = ""
    Track_number: str = ""
    Disk_number: str = ""


def get_list_of_files(chosen_dir):
    if chosen_dir.is_dir():
        return [child.as_posix() for child in chosen_dir.iterdir()]


def check_tags(directory: list):
    for file in directory:
        tags = taglib.File(file)
        audio_tags[file] = str(tags.tags)
        audio_tags[file] = Tag(
            tags.tags.get('ARTIST'), tags.tags.get('TITLE'), tags.tags.get('ALBUM'), tags.tags.get('ALBUMARTIST'),
            tags.tags.get('DATE'), tags.tags.get('GENRE'), tags.tags.get('TRACKNUMBER'), tags.tags.get('DISCNUMBER')
        )
        tags.close()
    print(audio_tags)


def main():
    class MainWindow(QMainWindow):
        def __init__(self):
            super().__init__()

            self.setWindowTitle("My App")
            self.setFixedSize(QSize(400, 400))
            button = QPushButton("Push me")
            button.clicked.connect(self.open_directory)
            self.setCentralWidget(button)

        def open_directory(self):
            filepath = QFileDialog.getExistingDirectory(self, 'Hey! Select a directory')
            audio_directory = Path(filepath)
            list_of_audio = get_list_of_files(audio_directory)
            check_tags(list_of_audio)

    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()

    app.exec()


if __name__ == "__main__":
    main()
