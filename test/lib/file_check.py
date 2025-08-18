from pathlib import Path

def file_exist(path: Path)  -> bool:
    return path.exists() and path.is_file()

def same_files(file_1: Path, file_2: Path) -> bool:
    return file_1.read_text() == file_2.read_text()
