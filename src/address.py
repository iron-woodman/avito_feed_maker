import os


class Address:
    MO_address = set()
    moskow_address = set()

    def __init__(self, company_name: str):
        self.company_name = company_name

    def load_MO_addresses(self):
        """
        загрузить список всех адресов по московской области
        :return:
        """
        file = f'company/{self.company_name}/address/oblast.txt'
        self.MO_address = self.load_address_set(file)

    def load_Moskow_addresses(self):
        """
        загрузить список всех адресов по московской области
        :return:
        """
        file = f'company/{self.company_name}/address/moskva_metro.txt'
        self.moskow_address = self.load_address_set(file)




    def load_product_text(self, product_name):
        txt_set = set()  # множество текстов
        txt_files = self.get_files_in_directory(f'company/{self.company_name}/TEXT/{product_name}/')
        for file in txt_files:
            data = self.load_txt_data(file)
            if data is not None:
                txt_set.add(data)
        return txt_set



    def load_address_set(self, file):
        with open(file, 'r', encoding='utf-8') as f:
            data = set(f.read().split('\n'))
            return data

    def get_moskow_address(self):
        '''
        получить московский адрес
        :param product:
        :return:
        '''
        if len(self.moskow_address) == 0:
            self.load_Moskow_addresses()
        cur_address = self.moskow_address.pop()
        return cur_address

    def get_MO_address(self):
        '''
        получить адрес в московской области
        :param product:
        :return:
        '''
        if len(self.MO_address) == 0:
            self.load_MO_addresses()
        cur_address = self.MO_address.pop()
        return cur_address
