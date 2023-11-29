import os.path

import requests
# https://drive.google.com/drive/folders/1c-5R3kdKPibLfQLu98SOaL4GiMmIHgC2?usp=sharing
# https://drive.google.com/drive/folders/1I1uc6c1y5ws0TJrpAmYHSxzJfWXVKeIo?usp=sharing
# https://disk.yandex.ru/d/rpkLbVp17Gjbow/6ab0008_1.jpg

def main():
    img_url_list = xml_parser.get_images_from_xml('AvMeb2022-02-01.xml')
    for url in img_url_list:
        try:
            url = url.replace("\\","/")
            file_name = url.split("/")[-1:]
            response = requests.get(url)
            if response.status_code == 200:
                if os.path.isdir('stol_img') is False:
                    os.mkdir('stol_img')
                with open('stol_img\\'+file_name[0],'wb') as f:
                    f.write(requests.get(url).content)  # get the content of the url and write/save in the created dir
                    f.close()  # stop writing/saving the image
        except Exception as e:
            print("Error:", e)
    print('Изображения загружены')

if __name__ == "__main__":
    main()