import json
from lxml import etree as ET
import os
import random
import datetime
# 48xaU%qb

company = 'artel_stroika'

IMG_FOLDER_BANI = f'{company}/bani'
IMG_FOLDER_BASSEIN = f'{company}/bassein'
IMG_FOLDER_DOM = f'{company}/dom'
IMG_FOLDER_HAMAM = f'{company}/hamam'
IMG_FOLDER_POMIVOCHNIE = f'{company}/pomivochnie'
IMG_FOLDER_SOLYANIE = f'{company}/solyanie'
IMG_FOLDER_SPA = f'{company}/spa'
IMG_FOLDER_OBORUD = f'{company}/oborud'

BANI_AD_COUNT_M = 1  #кол-во объявлений по БАНЯМ по москве
BASSEIN_AD_COUNT_M = 1 #кол-во объявлений по БАССЕЙНАМ по москве
DOM_AD_COUNT_M = 0  #кол-во объявлений по ДОМАМ по москве
HAMAM_AD_COUNT_M = 1  #кол-во объявлений по ХАМАМ по москве
POMIVOCHNIE_AD_COUNT_M = 1  #кол-во объявлений по ХАМАМ по москве
SOLYANIE_AD_COUNT_M = 1  #кол-во объявлений по ХАМАМ по москве
SPA_AD_COUNT_M = 1  #кол-во объявлений по ХАМАМ по москве
OBORUD_AD_COUNT_M = 0  #кол-во объявлений по оборудованию по москве

BANI_AD_COUNT_MO = 5  #кол-во объявлений по БАНЯМ по мос. обл.
BASSEIN_AD_COUNT_MO = 5 #кол-во объявлений по БАССЕЙНАМ по мос. обл.
DOM_AD_COUNT_MO = 0  #кол-во объявлений по ДОМАМ по мос. обл.
HAMAM_AD_COUNT_MO = 4  #кол-во объявлений по ХАМАМ по мос. обл.
POMIVOCHNIE_AD_COUNT_MO = 4  #кол-во объявлений по ХАМАМ по мос. обл.
SOLYANIE_AD_COUNT_MO = 3  #кол-во объявлений по ХАМАМ по мос. обл.
SPA_AD_COUNT_MO = 3  #кол-во объявлений по ХАМАМ по мос. обл.
OBORUD_AD_COUNT_MO = 0  #кол-во объявлений по оборудованию по мос. обл.

ARTICUL_PART = 'aug-'
AD_START_ID = 10301

ADDRESS_LIST_MOSKVA = f'{company}/address_moskva.json'
ADDRESS_LIST_OBLAST= f'{company}/address_oblast.json'
COMMON_JSON_FILE = f'{company}/common_data.json'
RESULT_FEED_NAME = f'{company}/{datetime.datetime.now().strftime("%Y-%m-%d").replace("-", "_")}.xml' # результирующий фид

BANI_AD_TEXT_FILE = f'{company}/bani.txt'
BASSEIN_AD_TEXT_FILE = f'{company}/bassein.txt'
DOM_AD_TEXT_FILE = f'{company}/dom.txt'
HAMAM_AD_TEXT_FILE = f'{company}/hamam.txt'
POMIVOCHNIE_AD_TEXT_FILE = f'{company}/pomivochnie.txt'
SOLYANIE_AD_TEXT_FILE = f'{company}/solyanie.txt'
SPA_AD_TEXT_FILE = f'{company}/spa.txt'
OBORUD_AD_TEXT_FILE = f'{company}/oborud.txt'

BANI_TITLES_FILE = f'{company}/bani_titles.txt'
BASSEIN_TITLES_FILE = f'{company}/bassein_titles.txt'
DOM_TITLES_FILE = f'{company}/dom_titles.txt'
HAMAM_TITLES_FILE = f'{company}/hamam_titles.txt'
POMIVOCHNIE_TITLES_FILE = f'{company}/pomivochnie_titles.txt'
SOLYANIE_TITLES_FILE = f'{company}/solyanie_titles.txt'
SPA_TITLES_FILE = f'{company}/spa_titles.txt'
OBORUD_TITLES_FILE = f'{company}/oborud_titles.txt'

# общие параметры во всех объявах
BASE_URL = f'https://biopoten-store.ru/avito/{company}/img/'


def create_avito_feed(ad_list, common_data):
    root = ET.Element('Ads', formatVersion="3", target="avito.ru")
    etree = ET.ElementTree(root)

    for index, ad in enumerate(ad_list):
        Id = ET.Element('Id')
        AdStatus = ET.Element('AdStatus')
        ManagerName = ET.Element('ManagerName')
        ContactPhone = ET.Element('ContactPhone')
        Address = ET.Element('Address')
        Category = ET.Element('Category')

        ImageUrls = ET.Element('ImageUrls')
        ImageNames = ET.Element('ImageNames')
        ServiceType = ET.Element('ServiceType')
        ServiceSubtype = ET.Element('ServiceSubtype')
        WorkTypes = ET.Element('WorkTypes')
        TeamSize = ET.Element('TeamSize')
        WorkTimeFrom = ET.Element('WorkTimeFrom')
        WorkTimeTo = ET.Element('WorkTimeTo')
        Guarantee = ET.Element('Guarantee')
        WorkExperience = ET.Element('WorkExperience')
        MaterialPurchase = ET.Element('MaterialPurchase')



        Title = ET.Element('Title')
        Price = ET.Element('Price')
        Description = ET.Element('Description')

        Id.text = ad['Id']
        AdStatus.text = common_data['AdStatus']
        ManagerName.text = common_data['ManagerName']
        ContactPhone.text = common_data['ContactPhone']
        Address.text = ad['Address']
        ImageUrls.text = ad['ImageUrls']
        ImageNames.text = ad['ImageNames']
        Category.text = common_data['Category']
        ServiceType.text = common_data['ServiceType']
        ServiceSubtype.text = common_data['ServiceSubtype']
        WorkTypes.text = ad['name']#common_data['WorkTypes']
        WorkExperience.text = common_data['WorkExperience']
        TeamSize.text = common_data['TeamSize']
        WorkTimeFrom.text = common_data['WorkTimeFrom']
        WorkTimeTo.text = common_data['WorkTimeTo']
        Guarantee.text = common_data['Guarantee']
        MaterialPurchase.text = common_data['MaterialPurchase']

        Title.text = ad['name']
        Price.text = ad['Price']

        ad_description = ad['description'] + f"\nАртикул: {ad['Articul']}\n"
        # ad_description = update_article(ad_description, ad['Articul'])
        Description.text = ET.CDATA(ad_description)

        offer = ET.Element('Ad')
        offer.append(Id)
        offer.append(AdStatus)
        offer.append(ManagerName)
        offer.append(ContactPhone)
        offer.append(Address)
        offer.append(Category)
        offer.append(ServiceType)
        offer.append(ServiceSubtype)
        offer.append(WorkTypes)
        offer.append(WorkExperience)
        offer.append(TeamSize)
        offer.append(WorkTimeFrom)
        offer.append(WorkTimeTo)
        offer.append(Guarantee)
        offer.append(MaterialPurchase)
        offer.append(Title)
        offer.append(Price)
        offer.append(Description)
        offer.append(ImageUrls)
        offer.append(ImageNames)
        root.append(offer)


    myfile = open(RESULT_FEED_NAME, "wb")
    etree.write(myfile, encoding='utf-8', xml_declaration=True, pretty_print=True)


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

def load_txt_data(file):
    with open(file, 'r', encoding='utf-8') as f:
        data = f.read()
        return data

if __name__ == "__main__":
    # генерируем списки цен по заданному диапазону
    bani_prices = [price for price in range(280000, 300000, 5000)]
    bassein_prices = [price for price in range(600000, 700000, 10000)]
    dom_prices = [price for price in range(6000000, 6500000, 100000)]
    hamam_prices = [price for price in range(550000, 600000, 10000)]
    pomivochnie_prices = [price for price in range(100000, 120000, 5000)]
    solyanie_prices = [price for price in range(140000, 150000, 5000)]
    spa_prices = [price for price in range(900000, 990000, 5000)]
    oborud_prices = [price for price in range(40000, 45000, 1000)]



    common_data = load_json_data(COMMON_JSON_FILE) # общие параметры
    address_list_moskva = load_txt_data(ADDRESS_LIST_MOSKVA)
    address_list_moskva = address_list_moskva.split('\n')
    address_list_mosobl = load_txt_data(ADDRESS_LIST_OBLAST)
    address_list_mosobl = address_list_mosobl.split('\n')

    # тексты
    bani_ad_txt = load_txt_data(BANI_AD_TEXT_FILE)
    bassein_ad_txt = load_txt_data(BASSEIN_AD_TEXT_FILE)
    dom_ad_txt = load_txt_data(DOM_AD_TEXT_FILE)
    hamam_ad_txt = load_txt_data(HAMAM_AD_TEXT_FILE)
    pomivochnie_ad_txt = load_txt_data(POMIVOCHNIE_AD_TEXT_FILE)
    solyanie_ad_txt = load_txt_data(SOLYANIE_AD_TEXT_FILE)
    spa_ad_txt = load_txt_data(SPA_AD_TEXT_FILE)
    oborud_ad_txt = load_txt_data(OBORUD_AD_TEXT_FILE)

    # заголовки
    bani_titles = load_txt_data(BANI_TITLES_FILE).split('\n')
    bassein_titles = load_txt_data(BASSEIN_TITLES_FILE).split('\n')
    dom_titles = load_txt_data(DOM_TITLES_FILE).split('\n')
    hamam_titles = load_txt_data(HAMAM_TITLES_FILE).split('\n')
    pomivochnie_titles = load_txt_data(POMIVOCHNIE_TITLES_FILE).split('\n')
    solyanie_titles = load_txt_data(SOLYANIE_TITLES_FILE).split('\n')
    spa_titles = load_txt_data(SPA_TITLES_FILE).split('\n')
    oborud_titles = load_txt_data(OBORUD_TITLES_FILE).split('\n')


    stol_titles = load_txt_data('s_titles.json').split('\n')
    um_titles = load_txt_data('um_titles.json').split('\n')
    p_titles = load_txt_data('podokonnik_titles.json').split('\n')

    if os.path.isdir(IMG_FOLDER_BANI):
        bani_images = os.listdir(IMG_FOLDER_BANI)

    if os.path.isdir(IMG_FOLDER_BASSEIN):
        bassein_images = os.listdir(IMG_FOLDER_BASSEIN)

    if os.path.isdir(IMG_FOLDER_DOM):
        dom_images = os.listdir(IMG_FOLDER_DOM)

    if os.path.isdir(IMG_FOLDER_HAMAM):
        hamam_images = os.listdir(IMG_FOLDER_HAMAM)

    if os.path.isdir(IMG_FOLDER_OBORUD):
        oborud_images = os.listdir(IMG_FOLDER_OBORUD)

    if os.path.isdir(IMG_FOLDER_POMIVOCHNIE):
        pomivochnie_images = os.listdir(IMG_FOLDER_POMIVOCHNIE)

    if os.path.isdir(IMG_FOLDER_SOLYANIE):
        solyanie_images = os.listdir(IMG_FOLDER_SOLYANIE)

    if os.path.isdir(IMG_FOLDER_SPA):
        spa_images = os.listdir(IMG_FOLDER_SPA)

    # множества изображений для каждой категории
    bani_images_set = set(bani_images.copy())
    bassein_images_set = set(bassein_images.copy())
    dom_images_set = set(dom_images.copy())
    hamam_images_set = set(hamam_images.copy())
    oborud_images_set = set(oborud_images.copy())
    pomivochnie_images_set = set(pomivochnie_images.copy())
    solyanie_images_set = set(solyanie_images.copy())
    spa_images_set = set(spa_images.copy())

    addresses_moskva = set(address_list_moskva.copy())
    addresses_mosobl = set(address_list_mosobl.copy())
    used_images_list = [] # список задействованных изображений


    common_ad_list = [] #общий список текстов объяв

    # ----------------область
    for index in range(BANI_AD_COUNT_MO):
        if len(addresses_mosobl) == 0:
            addresses_mosobl = set(address_list_mosobl.copy())
        common_ad_list.append({'name': random.choice(bani_titles), 'Address': addresses_mosobl.pop(), 'type': 'bani'})

    for index in range(BASSEIN_AD_COUNT_MO):
        if len(addresses_mosobl) == 0:
            addresses_mosobl = set(address_list_mosobl.copy())
        common_ad_list.append({'name': random.choice(bassein_titles), 'Address': addresses_mosobl.pop(), 'type': 'bassein'})

    for index in range(DOM_AD_COUNT_MO):
        if len(addresses_mosobl) == 0:
            addresses_mosobl = set(address_list_mosobl.copy())
        common_ad_list.append({'name': random.choice(dom_titles), 'Address': addresses_mosobl.pop(), 'type': 'dom'})

    for index in range(HAMAM_AD_COUNT_MO):
        if len(addresses_mosobl) == 0:
            addresses_mosobl = set(address_list_mosobl.copy())
        common_ad_list.append({'name': random.choice(hamam_titles), 'Address': addresses_mosobl.pop(), 'type': 'hamam'})

    # for index in range(OBORUD_AD_COUNT_MO):
    #     if len(addresses_mosobl) == 0:
    #         addresses_mosobl = set(address_list_mosobl.copy())
    #     common_ad_list.append({'name': random.choice(oborud_titles), 'Address': addresses_mosobl.pop(), 'type': 'oborud'})

    for index in range(POMIVOCHNIE_AD_COUNT_MO):
        if len(addresses_mosobl) == 0:
            addresses_mosobl = set(address_list_mosobl.copy())
        common_ad_list.append({'name': random.choice(pomivochnie_titles), 'Address': addresses_mosobl.pop(), 'type': 'pomivochnie'})

    for index in range(SOLYANIE_AD_COUNT_MO):
        if len(addresses_mosobl) == 0:
            addresses_mosobl = set(address_list_mosobl.copy())
        common_ad_list.append({'name': random.choice(solyanie_titles), 'Address': addresses_mosobl.pop(), 'type': 'solyanie'})

    for index in range(SPA_AD_COUNT_MO):
        if len(addresses_mosobl) == 0:
            addresses_mosobl = set(address_list_mosobl.copy())
        common_ad_list.append({'name': random.choice(spa_titles), 'Address': addresses_mosobl.pop(), 'type': 'spa'})

    # ----------------москва
    for index in range(BANI_AD_COUNT_M):
        if len(addresses_moskva) == 0:
            addresses_moskva = set(address_list_moskva.copy())
        common_ad_list.append({'name': random.choice(bani_titles), 'Address': addresses_moskva.pop(), 'type': 'bani'})

    for index in range(BASSEIN_AD_COUNT_M):
        if len(addresses_moskva) == 0:
            addresses_moskva = set(address_list_moskva.copy())
        common_ad_list.append({'name': random.choice(bassein_titles), 'Address': addresses_moskva.pop(), 'type': 'bassein'})

    for index in range(DOM_AD_COUNT_M):
        if len(addresses_moskva) == 0:
            addresses_moskva = set(address_list_moskva.copy())
        common_ad_list.append({'name': random.choice(dom_titles), 'Address': addresses_moskva.pop(), 'type': 'dom'})

    for index in range(HAMAM_AD_COUNT_M):
        if len(addresses_moskva) == 0:
            addresses_moskva = set(address_list_moskva.copy())
        common_ad_list.append({'name': random.choice(hamam_titles), 'Address': addresses_moskva.pop(), 'type': 'hamam'})

    # for index in range(OBORUD_AD_COUNT_M):
    #     if len(addresses_moskva) == 0:
    #         addresses_moskva = set(address_list_moskva.copy())
    #     common_ad_list.append({'name': random.choice(oborud_titles), 'Address': addresses_moskva.pop(), 'type': 'oborud'})

    for index in range(POMIVOCHNIE_AD_COUNT_M):
        if len(addresses_moskva) == 0:
            addresses_moskva = set(address_list_moskva.copy())
        common_ad_list.append({'name': random.choice(pomivochnie_titles), 'Address': addresses_moskva.pop(), 'type': 'pomivochnie'})

    for index in range(SOLYANIE_AD_COUNT_M):
        if len(addresses_moskva) == 0:
            addresses_moskva = set(address_list_moskva.copy())
        common_ad_list.append({'name': random.choice(solyanie_titles), 'Address': addresses_moskva.pop(), 'type': 'solyanie'})

    for index in range(SPA_AD_COUNT_M):
        if len(addresses_moskva) == 0:
            addresses_moskva = set(address_list_moskva.copy())
        common_ad_list.append({'name': random.choice(spa_titles), 'Address': addresses_moskva.pop(), 'type': 'spa'})

    ad_list = []

    for index, ad in enumerate(common_ad_list):
        picture1 = ''
        picture2 = ''
        picture3 = ''
        description = ''

        if ad['type'] == 'bani':
            price = random.choice(bani_prices)
            if len(bani_images_set) < 3:
                bani_images_set = set(bani_images.copy())
            picture1 = bani_images_set.pop()
            picture2 = bani_images_set.pop()
            picture3 = bani_images_set.pop()
            description = bani_ad_txt

        elif ad['type'] == 'bassein':
            price = random.choice(bassein_prices)
            if len(bassein_images_set) < 3:
                bassein_images_set = set(bassein_images.copy())
            picture1 = bassein_images_set.pop()
            picture2 = bassein_images_set.pop()
            picture3 = bassein_images_set.pop()
            description = bassein_ad_txt

        elif ad['type'] == 'dom':
            price = random.choice(dom_prices)
            if len(dom_images_set) < 3:
                dom_images_set = set(dom_images.copy())
            picture1 = dom_images_set.pop()
            picture2 = dom_images_set.pop()
            picture3 = dom_images_set.pop()
            description = dom_ad_txt

        elif ad['type'] == 'hamam':
            price = random.choice(hamam_prices)
            if len(hamam_images_set) < 3:
                hamam_images_set = set(hamam_images.copy())
            picture1 = hamam_images_set.pop()
            picture2 = hamam_images_set.pop()
            picture3 = hamam_images_set.pop()
            description = hamam_ad_txt

        elif ad['type'] == 'oborud':
            price = random.choice(oborud_prices)
            if len(oborud_images_set) < 3:
                oborud_images_set = set(oborud_images.copy())
            picture1 = oborud_images_set.pop()
            picture2 = oborud_images_set.pop()
            picture3 = oborud_images_set.pop()
            description = oborud_ad_txt

        elif ad['type'] == 'pomivochnie':
            price = random.choice(pomivochnie_prices)
            if len(pomivochnie_images_set) < 3:
                pomivochnie_images_set = set(pomivochnie_images.copy())
            picture1 = pomivochnie_images_set.pop()
            picture2 = pomivochnie_images_set.pop()
            picture3 = pomivochnie_images_set.pop()
            description = pomivochnie_ad_txt

        elif ad['type'] == 'solyanie':
            price = random.choice(solyanie_prices)
            if len(solyanie_images_set) < 3:
                solyanie_images_set = set(solyanie_images.copy())
            picture1 = solyanie_images_set.pop()
            picture2 = solyanie_images_set.pop()
            picture3 = solyanie_images_set.pop()
            description = solyanie_ad_txt

        elif ad['type'] == 'spa':
            price = random.choice(spa_prices)
            if len(spa_images_set) < 3:
                spa_images_set = set(spa_images.copy())
            picture1 = spa_images_set.pop()
            picture2 = spa_images_set.pop()
            picture3 = spa_images_set.pop()
            description = spa_ad_txt

        else:
            print(f"Тип объявлниея не определен: {ad['type']}")
            exit(1)

        ad['Price'] = str(price)
        ad['Articul'] = ARTICUL_PART + str(index + AD_START_ID)
        ad['Id'] = str(index + AD_START_ID)
        ad['ImageUrls'] = f'{BASE_URL + picture1} | {BASE_URL + picture2} | {BASE_URL + picture2}'
        ad['ImageNames'] = f'{picture1} | {picture2} | {picture2}'


        ad['description'] = description
        ad_list.append(ad.copy())
    print("всего объявлений:", str(len(ad_list)))

    random.shuffle(ad_list)
    create_avito_feed(ad_list, common_data)


