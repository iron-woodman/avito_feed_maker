import os.path
import xml.etree.ElementTree as ET
import random
import csv


F_DATA_CSV = 'f_data.csv'
S_DATA_CSV = 's_data.csv'
COMMON_DATA_CSV = 'common_data.csv'
SOURCE_XLM = 'Feed2022-02-01.xml'

def save_dict_to_csv(file, data):
    """
    сохранить данные в csv-файл
    :param file: имя результирующего файла
    :param data: словарь с данными
    :return:
    """
    with open(file, 'w', encoding='windows-1251') as f:
        w = csv.writer(f, delimiter=';', quotechar=',', quoting=csv.QUOTE_MINIMAL)
        w.writerow(data.keys())
        w.writerow(data.values())

def save_list_dict_to_csv(file, list_data):
    """
    сохранить данные (список слдоварей) в csv-файл
    :param file: имя результирующего файла
    :param list_data: список словарей с данными
    :return:
    """
    with open(file, 'w', encoding='utf-8') as f:
        w = csv.writer(f, delimiter=';', quotechar=',', quoting=csv.QUOTE_MINIMAL)
        for index, data in enumerate(list_data):
            if index == 0:
                w.writerow(data.keys())
            w.writerow(data.values())




def parse_feed_to_csv(source_xml_file, f_result_file, s_result_file):
    """
    парсинг xml- файла с последующим сохранением результатов в json-файлы
    :param source_xml_file: исходный фид
    :param f_result_file: json-файл с данными по фартукам
    :param s_result_file: json-файл с данными по столешницам
    :return:
    """
    tree = ET.parse(source_xml_file)
    root = tree.getroot()
    used_images_list = []  # список файлов изображений, которые попали в фид
    ad_counter = 1000  # счетчик объявлений

    f_ad_list = [] #фартуки
    s_ad_list = [] #столешницы
    s_titles = []
    s_descriptions = []
    f_titles = []
    f_descriptions = []
    adress_list = []

    for index, offer in enumerate(root.iter('Ad')):
        ad = dict()
        ad_counter += 1
        # date_publication = offer.find('datePublication')
        address = offer.find('Address')
        name = offer.find('Title')
        description = offer.find('Description')
        price = offer.find('Price')

        if index == 0:
            #общие параметры для всех объяв
            ad_status = offer.find('AdStatus')
            allow_email = offer.find('AllowEmail')
            ad_type = offer.find('AdType')
            manager_name = offer.find('ManagerName')
            contact_phone = offer.find('ContactPhone')
            category = offer.find('Category')
            goods_type = offer.find('GoodsType')
            condition = offer.find('Condition')
            common_data = {
              'AdStatus': ad_status.text,
              'AllowEmail': allow_email.text,
              'AdType': ad_type.text,
              'ManagerName': manager_name.text,
              'ContactPhone': contact_phone.text,
              'Category': category.text,
              'GoodsType': goods_type.text,
              'Condition': condition.text
            }

            save_dict_to_csv(COMMON_DATA_CSV, common_data)
        ad = {
              'address': address.text,
              'name': name.text,
              'description': description.text,
              'price': price.text
              }
        if 'фартук' in name.text.lower():
            f_ad_list.append(ad)
            if ad['name'] not in f_titles:
                f_titles.append(ad['name'])
            if ad['description'] not in f_descriptions:
                f_descriptions.append(ad['description'])
            if ad['address'] not in adress_list:
                adress_list.append(ad['address'])
        elif 'столешниц' in name.text.lower():
            s_ad_list.append(ad)
            if ad['name'] not in s_titles:
                s_titles.append(ad['name'])
            if ad['description'] not in s_descriptions:
                s_descriptions.append(ad['description'])
            if ad['address'] not in adress_list:
                adress_list.append(ad['address'])

    save_list_dict_to_csv(f_result_file, f_ad_list)
    save_list_dict_to_csv(s_result_file, s_ad_list)


    # with open(f_result_file, 'w', encoding='utf-8') as f:
    #     json.dump(f_ad_list, f, ensure_ascii=False, indent=4, separators=(',', ': '))
    #
    # with open(s_result_file, 'w', encoding='utf-8') as f:
    #     json.dump(s_ad_list, f, ensure_ascii=False, indent=4, separators=(',', ': '))
    #
    # with open('address_list.json', 'w', encoding='utf-8') as f:
    #     f.writelines("\n".join(adress_list))
    #     # json.dump(adress_list, f, ensure_ascii=False, indent=4, separators=(',', ': '))
    #
    # with open('s_titles.json', 'w', encoding='utf-8') as f:
    #     f.writelines("\n".join(s_titles))
    # with open('s_descriptions.json', 'w', encoding='utf-8') as f:
    #     f.writelines("\n".join(s_descriptions))
    #
    # with open('f_titles.json', 'w', encoding='utf-8') as f:
    #     f.writelines("\n".join(f_titles))
    # with open('f_descriptions.json', 'w', encoding='utf-8') as f:
    #     # f.writelines("\n".join(f_descriptions))
    #     json.dump(f_descriptions, f, ensure_ascii=False, indent=4, separators=(',', ': '))



def main():
    parse_feed_to_csv(SOURCE_XLM, F_DATA_CSV, S_DATA_CSV)
    print('работа завершена')


if __name__ == "__main__":
    main()


