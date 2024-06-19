## -*- coding: utf-8 -*-
import json
from lxml import etree as ET
import os
import random
import datetime

from src.texts import Text
from src.img import Img
from src.address import Address
from src.characteristics import Characteristics
from src.prices import Price
from src.titles import Title


# нужную из кампаний переместите на последнюю позицию
# т.е. в таком варианте генерация будет для stolishnici
# скрипт будет брать заголовки, тексты и фото из соответсвующего каталога
company = 'stolishnici'
company = 'new_account'
company = 'artel'
company = 'russian_fartuks'
company = 'artel'

# -----------------------------------------------------


#------------- кол-во объявлений -----------------------------------
UM_AD_COUNT_M = 20  #кол-во объявлений по умывальниам по москве
STOL_AD_COUNT_M = 200  #кол-во объявлений по столешницам по москве
POD_AD_COUNT_M = 10  #кол-во объявлений по подоконникам по москве

UM_AD_COUNT_MO = 20  #кол-во объявлений по умывальниам по мос. обл.
STOL_AD_COUNT_MO = 200  #кол-во объявлений по столешницам по мос. обл.
POD_AD_COUNT_MO = 10  #кол-во объявлений по подоконникам по мос. обл.
# -------------------------------------------------------------------

ARTICUL_PART = 'jun-' # префикс артикула
AD_START_ID = 23000 # стартовое значение числовой части артикула

#  общие настройки генерации для данной кампании (номер тлф., фио менеджера и т.д.)
COMMON_JSON_FILE = f'company/{company}/common_data.json'
# файл результирующиего xml-фида
RESULT_FEED_NAME = f'company/{company}/feeds/{datetime.datetime.now().strftime("%Y-%m-%d").replace("-", "_")}.xml'

# постоянная часть ссылки на фото (используется только если вы будут размещать фото на своем хостинге)
# если фото будете хранить на imgbb.com То данную настройку можно не трогать (она в скрипте не будет использована)
BASE_IMG_URL = '' #f'https://biopoten-store.ru/avito/{company}/img/'

# данный флаг определяет место хранения фото
# True  - изображения берем из готового файла со списком url
# False - изображения берем из локальных каталогов и после генерации грузим на свой хостинг,
# так же в этом случае будет использован параметр BASE_IMG_URL (см. выше)
IMG_URLS_FLAG = True

def load_json_data(file):
    try:
        if os.path.isfile(file) is False:
            print(f'Файл {file} не обнаружен.')
            return []
        with open(file, 'r', encoding='utf-8') as f:
            data = json.load(f)
            return data
    except Exception as e:
        print('load_json exception:', e)
        return []

def create_avito_feed(common_ad_list, common_data):
    '''
    основная функция генерации xml
    :param ad_list:
    :param common_data:
    :return:
    '''
    root = ET.Element('Ads', formatVersion="3", target="avito.ru")
    etree = ET.ElementTree(root)

    for index, ad in enumerate(common_ad_list):
        Id = ET.Element('Id')
        AdStatus = ET.Element('AdStatus')
        AllowEmail = ET.Element('AllowEmail')
        AdType = ET.Element('AdType')
        ManagerName = ET.Element('ManagerName')
        ContactPhone = ET.Element('ContactPhone')
        Address = ET.Element('Address')
        Category = ET.Element('Category')
        GoodsType = ET.Element('GoodsType')
        GoodsSubType = ET.Element('GoodsSubType')
        ComponentsType = ET.Element('ComponentsType')
        Condition = ET.Element('Condition')
        Availability = ET.Element('Availability')
        Title = ET.Element('Title')
        Price = ET.Element('Price')
        Description = ET.Element('Description')
        Image1 = ET.Element('Image')
        Image2 = ET.Element('Image')
        Image3 = ET.Element('Image')
        Image4 = ET.Element('Image')
        Image5 = ET.Element('Image')


        Id.text = ad['Id']
        AdStatus.text = common_data['AdStatus']
        AllowEmail.text = common_data['AllowEmail']
        AdType.text = common_data['AdType']
        ManagerName.text = common_data['ManagerName']
        ContactPhone.text = common_data['ContactPhone']
        Address.text = ad['Address']
        Category.text = common_data['Category']
        GoodsType.text = common_data['GoodsType']

        if ad['product'] == 'stol' or ad['product'] == 'um':
            GoodsSubType.text = common_data['GoodsSubType']
            ComponentsType.text = 'Столешницы'


        Condition.text = common_data['Condition']
        Availability.text = 'Под заказ'
        Title.text = ad['name']
        Price.text = ad['Price']

        Image1.set('url', ad['Image1'])
        Image2.set('url', ad['Image2'])
        Image3.set('url', ad['Image3'])
        Image4.set('url', ad['Image4'])


        Images = ET.Element('Images')
        Images.append(Image1)
        Images.append(Image2)
        Images.append(Image3)
        Images.append(Image4)


        ad_description = ad['description'] + f"{ad['Articul']}\n"
        # ad_description = update_article(ad_description, ad['Articul'])
        Description.text = ET.CDATA(ad_description)

        offer = ET.Element('Ad')
        offer.append(Id)
        offer.append(AdStatus)
        offer.append(AllowEmail)
        offer.append(AdType)
        offer.append(ManagerName)
        offer.append(ContactPhone)
        offer.append(Address)
        offer.append(Category)
        offer.append(GoodsType)
        if ad['product'] == 'stol' or ad['product'] == 'um':
            offer.append(GoodsSubType)
            offer.append(ComponentsType)
        offer.append(Condition)
        offer.append(Availability)
        offer.append(Title)
        offer.append(Price)
        offer.append(Description)
        offer.append(Images)
        root.append(offer)


    myfile = open(RESULT_FEED_NAME, "wb")
    etree.write(myfile, encoding='utf-8', xml_declaration=True, pretty_print=True)


def write_stat(common_ad_list_count):
    with open(f'log.txt', 'a', encoding='utf-8') as f:
        f.write('\n' + '*'*25)
        f.write(f"\n[{datetime.datetime.now().strftime('%Y-%m-%d')}] Компания: '{company}':")
        f.write(f"\nвсего объявлений: {common_ad_list_count}")
        f.write(f"\nстолешницы (Москва): {STOL_AD_COUNT_M}")
        f.write(f"\nстолешницы (Мос.обл.): {STOL_AD_COUNT_MO}")
        f.write(f"\nумывальники (Москва): {UM_AD_COUNT_M}")
        f.write(f"\nумывальники (Мос.обл.): {UM_AD_COUNT_MO}")
        f.write(f"\nумывальники (Москва): {POD_AD_COUNT_M}")
        f.write(f"\nумывальники (Мос.обл.): {POD_AD_COUNT_MO}")

        print(f"Компания: '{company}':")
        print("всего объявлений:", common_ad_list_count)
        print("столешницы (Москва):", STOL_AD_COUNT_M)
        print("столешницы (Мос.обл.):", STOL_AD_COUNT_MO)
        print("умывальники (Москва):", UM_AD_COUNT_M)
        print("умывальники (Мос.обл.):", UM_AD_COUNT_MO)
        print("умывальники (Москва):", POD_AD_COUNT_M)
        print("умывальники (Мос.обл.):", POD_AD_COUNT_MO)

def union_lists(list1: list, list2: list) -> list:
    """
    объединение списков с равномерным распределением элементов внутри них
    :param list1:
    :param list2:
    :return:
    """
    res_list=[]
    big_list = []
    small_list = []

    if len(list1) > len(list2):
        proportion = int(len(list1) / len(list2))
        small_list = list2
        big_list = list1
    else:
        proportion = int(len(list2) / len(list1))
        small_list = list1
        big_list = list2

    big_list_elements_counter = 0
    for item in big_list:
        res_list.append(item)
        big_list_elements_counter += 1
        if big_list_elements_counter == proportion:
            if len(small_list) > 0:
                res_list.append(small_list[0])
                small_list.remove(small_list[0])
            big_list_elements_counter = 0

    while len(small_list) > 0:
        res_list.insert(random.randint(0, len(res_list)), small_list[0])
        small_list.remove(small_list[0])

    return res_list

if __name__ == "__main__":
    common_data = load_json_data(COMMON_JSON_FILE)  # общие параметры
    text = Text(company_name=company, products=['podokonnik', 'stol', 'um'])
    img = Img(company_name=company, products=['podokonnik', 'stol', 'um'], img_count=4)
    address = Address(company_name=company)
    characteristics = Characteristics('colors.txt')
    price = Price()
    title = Title()
    characteristics = Characteristics('colors.txt')

    common_MO_ad_list = []  # общий список объявлений по области
    common_Moskow_ad_list = []  # общий список объявлений по Москве

    for index in range(UM_AD_COUNT_MO):
        common_MO_ad_list.append({'product': 'um', 'name': title.get_um_title(), 'Address': address.get_MO_address()})

    for index in range(POD_AD_COUNT_MO):
        common_MO_ad_list.append(
            {'product': 'podokonnik', 'name': title.get_pod_title(), 'Address': address.get_MO_address()}
        )

    for index in range(STOL_AD_COUNT_MO):
        common_MO_ad_list.append(
            {'product': 'stol', 'name': title.get_stol_title(), 'Address': address.get_MO_address()}
        )

    for index in range(UM_AD_COUNT_M):
        common_Moskow_ad_list.append(
            {'product': 'um', 'name': title.get_um_title(), 'Address': address.get_moskow_address()}
        )

    for index in range(POD_AD_COUNT_M):
        common_Moskow_ad_list.append(
            {'product': 'podokonnik', 'name': title.get_pod_title(), 'Address': address.get_moskow_address()}
        )

    for index in range(STOL_AD_COUNT_M):
        common_Moskow_ad_list.append(
            {'product': 'stol', 'name': title.get_stol_title(), 'Address': address.get_moskow_address()}
        )



# -----------------------------------------------------------------------------------------------------------------

    moskow_ad_list = []
    add_index = 1
    for ad in common_Moskow_ad_list:
        product = ad['product']
        ad['Price'] = str(price.get_price(product))
        ad['Articul'] = characteristics.get_full_row() + '\nАртикул:' + ARTICUL_PART + str(index + AD_START_ID)
        ad['Id'] = str(index + AD_START_ID)
        ad['Image1'] = BASE_IMG_URL + img.get_url(product, 1)
        ad['Image2'] = BASE_IMG_URL + img.get_url(product, 2)
        ad['Image3'] = BASE_IMG_URL + img.get_url(product, 3)
        ad['Image4'] = BASE_IMG_URL + img.get_url(product, 4)
        ad['description'] = text.get_text(product).replace('{HEADER}', ad['name'])
        ad['Id'] = str(add_index + AD_START_ID)
        add_index += 1
        moskow_ad_list.append(ad.copy())

    MO_ad_list = []

    for ad in common_MO_ad_list:
        product = ad['product']
        ad['Price'] = str(price.get_price(product))
        ad['Articul'] = characteristics.get_full_row() + '\nАртикул:' + ARTICUL_PART + str(index + AD_START_ID)
        ad['Id'] = str(index + AD_START_ID)
        ad['Image1'] = BASE_IMG_URL + img.get_url(product, 1)
        ad['Image2'] = BASE_IMG_URL + img.get_url(product, 2)
        ad['Image3'] = BASE_IMG_URL + img.get_url(product, 3)
        ad['Image4'] = BASE_IMG_URL + img.get_url(product, 4)
        ad['description'] = text.get_text(product).replace('{HEADER}', ad['name'])
        ad['Id'] = str(add_index + AD_START_ID)
        add_index += 1
        MO_ad_list.append(ad.copy())

    # перемешиваем
    random.shuffle(moskow_ad_list)
    random.shuffle(MO_ad_list)

    #----- делаем равномерное распределение объявлений
    common_ad_list = union_lists(moskow_ad_list, MO_ad_list)


    # генерируем feed
    create_avito_feed(common_ad_list, common_data)
    write_stat(len(common_ad_list))


