from dataclasses import dataclass
import taglib
from pathlib import Path

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
    chosen_dir = Path(chosen_dir)
    if chosen_dir.is_dir():
        return [child.as_posix() for child in chosen_dir.iterdir()]


def check_tags(directory: list):
    audio_tags = {}
    for file in directory:
        tags = taglib.File(file)
        audio_tags[file] = str(tags.tags)
        audio_tags[file] = Tag(
            tags.tags.get('ARTIST'), tags.tags.get('TITLE'), tags.tags.get('ALBUM'), tags.tags.get('ALBUMARTIST'),
            tags.tags.get('DATE'), tags.tags.get('GENRE'), tags.tags.get('TRACKNUMBER'), tags.tags.get('DISCNUMBER')
        )
        tags.close()
    print(audio_tags)
