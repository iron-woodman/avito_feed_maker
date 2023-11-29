import requests
from bs4 import BeautifulSoup


def parse_all_colors(url):
    responce = requests.get(url)
    color_list = []
    if responce.ok:
        soup = BeautifulSoup(responce.content, features='lxml')
        mydivs = soup.find_all("div", {"class": "color-block"})

        for div in mydivs:
            color_list.append(div.text)
        return color_list


def main():
    color_list = parse_all_colors('https://xn----8sbicjmbdfi2b8a3a.xn--p1ai/dlya-proizvoditeley-stoleshnits/tsveta-granistone/')
    print(color_list)

# <div class="color-block" data-id="5426"><img src="/upload/iblock/646/646580cf0c7d565ad8dd199b5c2c53f4.jpg" alt="Жидкий гранит GraniStone, коллекция Natural, арт. 001 Крокус"><p>001 Крокус</p></div>
if __name__ == "__main__":
    main()