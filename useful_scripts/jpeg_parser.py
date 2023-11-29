import time
import requests
from bs4 import BeautifulSoup
import os

URL = 'https://avitovtop.ru/artel_youla/'
FOLDER = 'artel_youla_img'


def save_images_to_folder(url_list, folder):
    exist_files = []
    if not os.path.exists(folder):
        os.makedirs(folder)
    else:
        exist_files = os.listdir(folder)

    for url in url_list:
        file_name = url.split("/")[-1:][0]
        if file_name == "":
            continue
        elif file_name in exist_files:
            continue

        responce = requests.get(url)
        if responce.ok:

            file_path = folder + "\\" +  file_name
            print(file_path)
            with open(file_path,
                      'wb') as f:  # open the image as the mentioned file format, (w for writing, and b for binary)
                # as the format is jpg, it needs to be saved as a binary file
                # here "f" is just a variable assignment
                f.write(responce.content)  # get the content of the url and write/save in the created dir
                f.close()  # stop writing/saving the image
        time.sleep(1)



def parse_all_images(url, result_folder):
    responce = requests.get(url)
    if responce.ok:
        soup = BeautifulSoup(responce.content, features='lxml')
        links = soup.findAll('a')
        url_list = []
        for link in links:
            url_list.append(URL + link.get('href'))
        save_images_to_folder(url_list, result_folder)
        print("работа завершена")

def main():
    parse_all_images(URL, FOLDER)


if __name__ == "__main__":
    main()
