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
    'documents': ['.pdf', '.txt', '.doc', '.docx', '.rtf', '.pptx', '.ppt', '.xlsx', '.xls']
}
# py sort.py i:/Users/rostislav.ATEM/Desktop/Мотлох/
# key names will be folder names!
# main_path = 'C:/Users/Rost/Desktop/Мотлох1/'
# main_path = 'I:\\Users\\rostislav.ATEM\\Desktop\\Мотлох2'
# folder_path = 'C:/Users/Rost/Desktop/Мотлох1'
# py sort-new-path.py I:\\Users\\rostislav.ATEM\\Desktop\\Мотлох2
# path = 'I:\\Users\\rostislav.ATEM\\Desktop\\Мотлох2'


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
    print(extract_dir)
    for elem in extract_dir.glob("**/"):
        print(elem.name)
        target_dir = extract_dir.joinpath(f'{extract_dir}\{elem.stem}')
        print(target_dir)
        target_dir.mkdir()
    # new_name = target_dir.joinpath(f"{normalize(file.stem)}{file.suffix}")
        shutil.unpack_archive(elem, target_dir)
        # os.remove(elem)
        continue
    # try:
    # except ValueError:
    # new_name = target_dir.joinpath(f"{normalize(file.stem)}{file.suffix}")
    # shutil.unpack_archive(filename[, extract_dir[, format[, filter]]])
    return


def get_extension(file: Path) -> str:
    ext = file.suffix.lower()
    # print(ext)
    for key, values in extensions.items():
        if ext in values:
            # print(key)
            return key
    return "unknown"


def main():
    try:
        path = Path(sys.argv[1])
    except IndexError:
        return "No path to folder"

    if not path.exists():
        return f"Folder with path {path} dos`n exists."
    sort_folder(path)
    return "All ok"


def move_file(file: Path, root_dir: Path, categorie: str) -> None:
    target_dir = root_dir.joinpath(categorie)
    # print(target_dir)
    if not target_dir.exists():
        target_dir.mkdir()
    new_name = target_dir.joinpath(f"{normalize(file.stem)}{file.suffix}")
    # print(file.stem)

    # if new_name.exists():
    # print(new_name)
    # new_name = new_name.with_name(
    #    f"{new_name.stem}-{uuid.uuid4()}{file.suffix}")
    file.replace(new_name)


def sort_folder(path: Path) -> None:
    for elem in path.glob("**/*"):
        # print(elem)
        if elem.is_file():
            extension = get_extension(elem)
            move_file(elem, path, extension)
            # if extension == 'archives':
            #    extract_file(elem)
    extract_file(path)
    del_empty_dirs(path)
    # extract_file(path)


# main_path = 'C:/Users/Rost/Desktop/Мотлох/'
# folder_path = 'I:\\Users\\rostislav.ATEM\\Desktop\\Мотлох'
# py sort.py i:/Users/rostislav.ATEM/Desktop/Мотлох
# main_path = sys.argv[1]


if __name__ == "__main__":
    print(main())
