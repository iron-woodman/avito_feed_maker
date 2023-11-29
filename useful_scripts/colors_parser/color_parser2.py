import requests
from bs4 import BeautifulSoup


def parse(html: str) -> list:
    soup = BeautifulSoup(html, 'lxml')

    colors = []
    mydivs = soup.find_all("div", {"class": "color-block"})
    print(mydivs)


    sibling = soup.find('div', {'class': "color-block"})
    while sibling:
        if sibling['class'] == ['event__header']:
            title = sibling.find('span', {'class': 'event__title--type'}).getText()
        else:
            participant_1 = sibling.find('div', {'class': 'event__participant'})
            participant_2 = participant_1.find_next_sibling('div')
            colors.append({'league': title, 'participants': [participant_1.getText(), participant_2.getText()]})

        sibling = sibling.find_next_sibling('div')

    return colors


if __name__ == '__main__':
    colors = []

    with open('f:/color_html/1.txt') as f:
        txt = f.read()
        parts = txt.split("арт. ")
        for part in parts:
            color = part.split("</a>")[0]
            if len(color) > 20 or '<p>' in color or len(color) < 2:
                continue
            colors.append(color)
        print(len(colors))
        print(colors)
    with open('colors.txt', 'w', encoding='utf-8') as f:
        f.writelines("%s\n" % line for line in colors)



    # with open('f:/color_html/759 цветов GraniStone.html') as f:
    #     html = f.read()
    #
    # matches = parse(html)

