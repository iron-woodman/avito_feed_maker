from lxml import etree as ET
import random

source_feed = '2022_10_31.xml'
result_feed = 'result.xml'
new_headers = ['Столешницы из акрилового камня',
               'Cтолешницы из кварцевого агломерата',
               'Cтолешницы из акрила',
               'Cтолешницы из кварца']


def get_images_from_xml(xml_file):
    root = ET.parse(xml_file)
    image_list = []
    for img in root.iter('Image'):
        print(img.attrib['url'])
        image_list.append(img.attrib['url'])
    return image_list


def update_article(desc_text, new_article):
    part = '<p><strong>Артикул: </strong>'
    pos = desc_text.find(part)
    if pos < 0:
        print("артикул не найден")
        return desc_text
    substr = desc_text[pos+len(part):]
    part = '</p>'
    pos = substr.find(part)
    article = substr[:pos]
    desc_text = desc_text.replace(article, new_article)
    return  desc_text



# def update_xml_prices_and_imagesurls(source_xml_file, fprices, sprices, stol_img_list, fart_img_list):
#
#     fimages = set(fart_img_list)
#     simages = set(stol_img_list)
#     #
#     # for image in img_file_list:
#     #     if image[0] == 's':
#     #         simages.add(BASE_IMG_URL + "/" + image)
#     #     elif image[0] == 'f':
#     #         fimages.add(BASE_IMG_URL + "/" + image)
#
#
#
#     tree = ET.parse(source_xml_file)
#     root = tree.getroot()
#     used_images_list = [] # список файлов изображений, которые попали в фид
#     ad_counter = 1000 # счетчик объявлений
#     for ad in root.iter('Ad'):
#         ad_counter += 1
#         id = ad.find('Id')
#         id.text = 'ad' + str(ad_counter)
#         title = ad.find('Title').text.lower()
#         price = ad.find('Price')
#         # manager = ad.find('ManagerName')
#         # manager.text = MANAGER_NAME
#         # phone = ad.find('ContactPhone')
#         # phone.text = PHONE
#         description = ad.find("Description")
#         desc_text = description.text
#
#         images = ad.find('Images')
#         img_list = images.findall('Image')
#         print(title)
#         if title.find('фартук') > -1:
#             desc_text = update_article(desc_text, "fart-"+str(ad_counter))
#             price.text = str(random.choice(fprices))
#             for image in img_list:
#                 new_image = fimages.pop()
#                 used_images_list.append(IMG_FOLDER_FART + "\\"+new_image)
#                 image.set('url', BASE_IMG_URL + "/" + new_image)
#         elif title.find('столешница') > -1:
#             desc_text = update_article(desc_text, "stol-" + str(ad_counter))
#             price.text = str(random.choice(sprices))
#             for image in img_list:
#                 new_image = simages.pop()
#                 used_images_list.append(IMG_FOLDER_STOL + "\\"+new_image)
#                 image.set('url', BASE_IMG_URL + "/" + new_image)
#         else:
#             print(title, '-- категория не определена')
#         description.text = desc_text
#
#
#     with open('result.xml', 'wb') as f:
#         # tree.write(f, encoding='utf-8')
#         tree.write(f, encoding='utf-8')
#
#     print("Всего объявлений:", str(ad_counter - 1000))
#
#     # переносим отобранные объявления
#     for image in used_images_list:
#         source = image
#         result = IMG_FOLDER_RESULT + "\\" + os.path.basename(image)
#         os.replace(image, result)



def update_headers_in_feed(source_xml_file, result_feed):
    '''
    :param source_xml_file: исходный xml-файл
    :return:
    '''
    global new_headers
    new_headers_count = 30

    tree = ET.parse(source_xml_file)
    root = tree.getroot()
    new_ad_count = dict()
    for header in new_headers:
        new_ad_count[header] = 0

    for ad in root.iter('Ad'):
        new_header = random.choice(new_headers)

        title = ad.find('Title')
        title_text = title.text
        description = ad.find("Description")
        desc_text = description.text
        if new_ad_count[new_header] >= new_headers_count or 'столешниц' not in title_text.lower():
            description.text = ET.CDATA(description.text)
            continue
        title.text = new_header
        description.text = ET.CDATA(desc_text.replace(title_text, new_header))
        new_ad_count[new_header] = new_ad_count[new_header] + 1

    with open(result_feed, 'wb') as f:
        # tree.write(f, encoding='utf-8')
        tree.write(f, encoding='utf-8', xml_declaration=True, pretty_print=True)


def main():
    global source_feed
    global result_feed

    update_headers_in_feed(source_xml_file=source_feed, result_feed=result_feed)
    # # фартуки 1500 до 2500, на столешницы от 4500 до 5500
    #
    # fprices = [price for price in range(1500, 2600, 100)]
    # sprices = [price for price in range(4500, 5600, 100)]
    #
    # if os.path.isdir(IMG_FOLDER_STOL):
    #     stol_images = os.listdir(IMG_FOLDER_STOL)
    #
    # if os.path.isdir(IMG_FOLDER_FART):
    #     fart_images = os.listdir(IMG_FOLDER_FART)
    #
    # update_xml_prices_and_imagesurls(SOURCE_XLM, fprices, sprices, stol_images, fart_images)
    print('работа завершена')


if __name__ == "__main__":
    main()



