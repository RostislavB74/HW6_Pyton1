import os
import sys
import re
import shutil
from pathlib import Path
from glob import glob
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

normalized_name = []


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


def match(file, alphabet=set('абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ')):
    return not alphabet.isdisjoint(file)


def normalize(file_for_translate):
    new_name = []
    map_translate_ord = {
        1072: 'a', 1073: 'b', 1074: 'v', 1075: 'h', 1076: 'd', 1077: 'e', 1105: 'e', 1078: 'zh', 1079: 'z',
        1080: 'y', 1081: 'i', 1082: 'k', 1083: 'l', 1084: 'm', 1085: 'n', 1086: 'o', 1087: 'p', 1088: 'r',
        1089: 's', 1090: 't', 1091: 'u', 1092: 'f', 1093: 'kh', 1094: 'ts', 1095: 'ch', 1096: 'sh', 1097: 'shch',
        1098: '', 1099: 'y', 1100: '', 1101: 'e', 1102: 'iu', 1103: 'ia', 1108: 'ie', 1110: 'i', 1111: 'i',
        1169: 'g', 1040: 'A', 1041: 'B', 1042: 'V', 1043: 'H', 1044: 'D', 1045: 'E', 1025: 'E', 1046: 'ZH',
        1047: 'Z', 1048: 'Y', 1049: 'I', 1050: 'K', 1051: 'L', 1052: 'M', 1053: 'N', 1054: 'O', 1055: 'P',
        1056: 'R', 1057: 'S', 1058: 'T', 1059: 'U', 1060: 'F', 1061: 'KH', 1062: 'TS', 1063: 'CH', 1064: 'SH',
        1065: 'SHCH', 1066: '', 1067: 'Y', 1068: '', 1069: 'E', 1070: 'IU', 1071: 'IA', 1028: 'IE', 1030: 'I',
        1031: 'I', 1168: 'G'
    }

    for elem in file_for_translate:
        new_name.append(elem.translate(map_translate_ord).replace(' ', '_'))
    # print(new_name)
    return new_name


if __name__ == "__main__":
#main_path = 'C:/Users/Rost/Desktop/Мотлох/'
    folder_path = 'I:\\Users\\rostislav.ATEM\\Desktop\\Мотлох'
#py sort.py i:/Users/rostislav.ATEM/Desktop/Мотлох
    #main_path = sys.argv[1]
    create_folders_from_extension(folder_path, extensions)
    
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
                    # print(path_separate)
                    file_for_translate = path_separate
                    normalized_name = (normalize(file_for_translate))
                    new_name = '.'.join(normalized_name)
                    folder = ext_list[dict_key_int][0]
                    if folder =='archives':
                        try:
                            shutil.unpack_archive(path, os.path.join(f'{folder_path}\\archives\\{new_name}'), extension)
                            print (path)
                            os.remove(path)
                        except ValueError:
                            continue
                        break
                new_path = os.path.join(f'{folder_path}\\{folder}\\', new_name)
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
    del_empty_dirs(folder_path)
    

