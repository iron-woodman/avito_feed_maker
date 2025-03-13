## -*- coding: utf-8 -*-
 # этот скрипт делает файлы ссылок на основе выбранной компании (базовом URL)
import shutil
import os

from useful_scripts.xml_feed_updater import result_feed

company = 'stolishnici'
company = 'new_account'
company = 'artel'
company = 'russian_fartuks'
company = 'artel'

# корневой каталог изображений компании, внутри они раскиданы по категориям (um, podokonnik, stol)
# и номерам фото в объявлении от 1 до 4
COMMON_IMG_FOLDER = f'company/{company}/IMG'
COMMON_IMG_URLS_FOLDER = f'company/{company}/IMG_URLS'
DOMEN_NAME = 'https://an-stone.ru/av/'
# базовый урл хостинга
BASE_IMG_URL = f'https://an-stone.ru/av/{company}/' #f'https://biopoten-store.ru/avito/{company}/img/'

# https://an-stone.ru/av/artel/stol/1/photos_23.jpg

def find_subdirectories_listdir(directory):
    """Находит все подкаталоги в указанном каталоге (менее эффективный вариант)."""
    subdirectories = []
    try:
        for item in os.listdir(directory):
            item_path = os.path.join(directory, item)
            if os.path.isdir(item_path):
                subdirectories.append(item_path)
    except FileNotFoundError:
        print(f"Каталог '{directory}' не найден.")
        return []
    except OSError as e:
        print(f"Ошибка при доступе к каталогу: {e}")
        return []

    return subdirectories

#
# def rename_jpg_files(directory, mask):
#     global BASE_IMG_URL
#     global DOMEN_NAME
#
#     result_urls = []
#     dir_path = pathlib.Path(directory)
#     jpg_files = sorted([f for f in dir_path.glob("*.jpg")])  # более эффективный способ поиска файлов
#
#     for i, file_path in enumerate(jpg_files):
#         new_filename = f"{mask}_{i + 1}.jpg"
#         new_path = dir_path / new_filename
#         # new_path = (new_path.absolute().replace('company/', DOMEN_NAME))
#         print(new_path.with_name())
#         result_urls.append(new_path)
#         try:
#             if new_path.exists():
#                 new_path.unlink()
#                 print(f"Удалён существующий файл: {new_filename}")
#             file_path.rename(new_path)
#             print(f"Переименован файл: {file_path.name} -> {new_filename}")
#
#         except OSError as e:
#             print(f"Ошибка при переименовании файла {file_path.name}: {e}")
#     return result_urls

def rename_jpg_files(directory, mask):
    """
    Находит все JPG файлы в указанном каталоге и переименовывает их, перезаписывая существующие файлы.
    Использует os.path.normpath() для обработки путей.
    """
    result_urls = []
    try:
        jpg_files = [f for f in os.listdir(directory) if f.lower().endswith('.jpg')]
        jpg_files.sort()
    except Exception as e:
        print(e)

    for i, filename in enumerate(jpg_files):
        file_path = os.path.normpath(os.path.join(directory, filename))
        url = file_path.replace('company\\', DOMEN_NAME)
        url = url.replace('\\','/')
        result_urls.append(url)

    return result_urls


def store_urls_to_file(res_urls_path, res_urls):
    try:
        if os.path.exists(res_urls_path):
            os.remove(res_urls_path)
        with open(res_urls_path, 'w', encoding='utf-8') as f:
            for item in res_urls:
                f.writelines(str(item) + '\n')
    except Exception as e:
        print(f"Ошибка сохранения ссылок в файл: '{e}'.")



def main():
    global company
    dirs = ['stol', 'podokonnik', 'um']
    for dir in dirs:
        sub_dirs = find_subdirectories_listdir(f'company/{company}/IMG/{dir}/')
        for photo_dir in sub_dirs:
            res_urls = rename_jpg_files(photo_dir, dir)
            print(res_urls)
            if len(res_urls) > 0:
                last_dir = photo_dir.split('/')[-1]
                res_urls_path = COMMON_IMG_URLS_FOLDER +"/"+dir+"/"+f"img{last_dir}_urls.txt"
                store_urls_to_file(res_urls_path, res_urls)



if __name__ == "__main__":
    main()