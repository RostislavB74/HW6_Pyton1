import os
import sys
import shutil
from pathlib import Path
from glob import glob
from normalize import normalize

extensions = {
    'video': ['.mp4', '.mov', '.avi', '.mkv'],
    'audio': ['.mp3', '.wav', '.ogg', '.amr'],
    'images': ['.jpg', '.png', '.jpeg', '.svg'],
    'archives': ['.zip', '.rar', '.gz','.tar'],
    'documents': ['.pdf', '.txt', '.doc', '.docx', '.rtf', '.pptx', '.ppt', '.xlsx', '.xls']
}
#py sort.py i:/Users/rostislav.ATEM/Desktop/Мотлох/
# key names will be folder names!
#main_path = 'C:/Users/Rost/Desktop/Мотлох1/'
#main_path = 'I:\\Users\\rostislav.ATEM\\Desktop\\Мотлох2'
#folder_path = 'C:/Users/Rost/Desktop/Мотлох1'
#path = 'I:\\Users\\rostislav.ATEM\\Desktop\\Мотлох2'

def del_empty_dirs(path):
    
    for d in os.listdir(path):
        a = os.path.join(path, d)
        if os.path.isdir(a):
            del_empty_dirs(a)
            if not os.listdir(a):
                os.rmdir(a)
                print(a, 'видалена')

def get_extension(file: Path) -> str:
    ext = file.suffix.lower()
    #print(ext)
    for key, values in extensions.items():
        if ext in values:
            #print(key)
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


def sort_folder(path: Path) -> None:
    for elem in path.glob("**/*"):
        print(elem)
        if elem.is_file():
            extension = get_extension(elem)
            print(extension)
            del_empty_dirs(path)
    

    # delete_emppty_folders(path)
    # upack_archive(path)
    
    

#main_path = 'C:/Users/Rost/Desktop/Мотлох/'
    #folder_path = 'I:\\Users\\rostislav.ATEM\\Desktop\\Мотлох'
#py sort.py i:/Users/rostislav.ATEM/Desktop/Мотлох
    #main_path = sys.argv[1]
    
    
   
    
if __name__ == "__main__":
    print(main())