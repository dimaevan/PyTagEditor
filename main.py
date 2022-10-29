import taglib
from pathlib import Path

selected_dir = Path("test/")
audio_dir = Path.cwd() / selected_dir
audio_files = []
audio_tags = {}

if audio_dir.is_dir():
    audio_files = [child.as_posix() for child in audio_dir.iterdir()]

for file in audio_files:
    tags = taglib.File(file)
    audio_tags[file] = str(tags.tags)
    tags.close()

print(audio_tags)
