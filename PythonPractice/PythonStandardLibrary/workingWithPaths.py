from pathlib import Path

path = Path(r"C:\Program Files\Microsoft") #r makes it a raw string

path.exists()
path.is_file()
path.is_dir()