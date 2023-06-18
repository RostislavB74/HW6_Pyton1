import os
import sys
import shutil
from pathlib import Path
import uuid
from normalize import normalize

extensions = {
    'video': ['.mp4', '.mov', '.avi', '.mkv'],
    'audio': ['.mp3', '.wav', '.ogg', '.amr'],
    'images': ['.jpg', '.png', '.jpeg', '.svg'],
    'archives': ['.zip', '.gz', '.tar'],
    'documents': ['.pdf', '.txt', '.doc', '.docx',
                  '.rtf', '.pptx', '.ppt', '.xlsx', '.xls']
}


def del_empty_dirs(path):
    for d in os.listdir(path):
        a = os.path.join(path, d)
        if os.path.isdir(a):
            del_empty_dirs(a)
            if not os.listdir(a):
                os.rmdir(a)
                print(a, 'видалена')


def extract_file(folder_path) -> None:
    extract_dir = folder_path.joinpath('archives')
    for elem in extract_dir.glob("*.*"):
        target_dir = extract_dir.joinpath(f"{extract_dir}\{elem.stem}")
        if not target_dir.exists():
            target_dir.mkdir()
        shutil.unpack_archive(elem, target_dir)
        os.remove(elem)
        continue
    return


def get_extension(file: Path) -> str:
    ext = file.suffix.lower()
    for key, values in extensions.items():
        if ext in values:
            return key
    return "unknown"


def main():
    try:
        path = Path(sys.argv[1])
    except IndexError:
        return "No path to folder"

    if not path.exists():
        return f"Folder with path {path} dosn't exists."
    sort_folder(path)
    return "All ok"


def move_file(file: Path, root_dir: Path, categorie: str) -> None:
    target_dir = root_dir.joinpath(categorie)
    if not target_dir.exists():
        target_dir.mkdir()
    new_name = target_dir.joinpath(f"{normalize(file.stem)}{file.suffix}")
    file.replace(new_name)


def sort_folder(path: Path) -> None:
    for elem in path.glob("**/*"):
        if elem.is_dir():
            if elem.stem in extensions.keys():
                continue
        if elem.is_file():
            extension = get_extension(elem)
            move_file(elem, path, extension)
    del_empty_dirs(path)
    extract_file(path)


if __name__ == "__main__":
    print(main())
