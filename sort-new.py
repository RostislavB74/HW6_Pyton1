import os
import sys
import re

import shutil
from pathlib import Path
from glob import glob
from normalize import normalize
#py sort.py i:/Users/rostislav.ATEM/Desktop/Мотлох/
# key names will be folder names!
#main_path = 'C:/Users/Rost/Desktop/Мотлох1/'
#main_path = 'I:\\Users\\rostislav.ATEM\\Desktop\\Мотлох2'

extensions = {
    'video': ['mp4', 'mov', 'avi', 'mkv'],
    'audio': ['mp3', 'wav', 'ogg', 'amr'],
    'images': ['jpg', 'png', 'jpeg', 'svg'],
    'archives': ['zip', 'rar', 'gz','tar'],
    'documents': ['pdf', 'txt', 'doc', 'docx', 'rtf', 'pptx', 'ppt', 'xlsx', 'xls']
}

#folder_path = 'C:/Users/Rost/Desktop/Мотлох1'
#folder_path = 'I:\\Users\\rostislav.ATEM\\Desktop\\Мотлох2'

def create_folders_from_extension(folder_path, folder_names):
    for folder in folder_names:
        if not os.path.exists(f'{folder_path}\\{folder}'):
            os.mkdir(f'{folder_path}\\{folder}')
        if not os.path.exists(f'{folder_path}\\unknown'):
            os.mkdir(f'{folder_path}\\unknown')

def del_empty_dirs(path):
    #if dirs != extensions:
    for d in os.listdir(path):
        a = os.path.join(path, d)
        if os.path.isdir(a):
            del_empty_dirs(a)
            if not os.listdir(a):
                os.rmdir(a)
                print(a, 'видалена')




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
    for item in path.glob("**/*"):
        print(item)
        if item.is_file():
            #cat = get_categories(item)
            del_empty_dirs(path)
    

    # delete_emppty_folders(path)
    # upack_archive(path)
    
    

#main_path = 'C:/Users/Rost/Desktop/Мотлох/'
    #folder_path = 'I:\\Users\\rostislav.ATEM\\Desktop\\Мотлох'
#py sort.py i:/Users/rostislav.ATEM/Desktop/Мотлох
    #main_path = sys.argv[1]
    
    create_folders_from_extension(path, extensions)
folder_path = path
for root, dirs, files in os.walk(folder_path):
    if dirs != extensions:
        for file in files:
            path = os.path.join(root, file)
            extension = file.split('.')[-1]
            ext_list = list(extensions.items())
            # print(ext_list)
            for dict_key_int in range(len(ext_list)):
                new_name = file
                folder = 'unknown'
                if extension in ext_list[dict_key_int][1]:
                    path_separate = file.split('.')
                    file_for_translate = path_separate
                    file_for_translate[0]= (normalize(file_for_translate[0]))
                    new_name = '.'.join(file_for_translate)
                    folder = ext_list[dict_key_int][0]
                    if folder =='archives':
                        try:
                            shutil.unpack_archive(path, os.path.join(f'{path}\\archives\\{new_name}'), extension)
                            print (path)
                            os.remove(path)
                        except ValueError:
                            continue
                        break
                new_path = os.path.join(f'{path}\\{folder}\\', new_name)
                try:
                        os.replace(path, new_path)

                except FileExistsError:
                    copy_new_name = new_name.split('.')
                    copy_new_name[-2] = copy_new_name[-2]+'_copy'
                    file = '.'.join(copy_new_name)
                    continue
                except PermissionError:
                    continue

                except FileNotFoundError:
                    continue
    del_empty_dirs(path)
    
if __name__ == "__main__":
    print(main('i:/Users/rostislav.ATEM/Desktop/Мотлох'))