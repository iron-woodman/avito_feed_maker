import os


class Text:

    product_texts = dict() # key=product, value=set(text1, text2, ...)

    def __init__(self, company_name:str, products: list):
        self.company_name = company_name
        self.products = products
        self.load_all_texts()

    def load_txt_data(file):
        with open(file, 'r', encoding='utf-8') as f:
            data = f.read()
            return data

    def load_all_texts(self):
        """
        загрузить список всех текстов по всем категориям товаров (столешницы, умывальники, подоконники)
        :return:
        """
        for product in self.products:
            self.product_texts[product] = self.load_product_text(product)

    def load_product_text(self, product_name):
        txt_set = set() # множество текстов
        txt_files = self.get_files_in_directory(f'company/{self.company_name}/TEXT/{product_name}/')
        for file in txt_files:
            data = self.load_txt_data(file)
            if data is not None:
                txt_set.add(data)
        return txt_set

    def get_files_in_directory(self, directory):
        """
        получить список файлов (полные пути в заданном катлоге)
        :param directory:
        :return:
        """
        files_list = [os.path.join(directory, file) for file in os.listdir(directory)]
        return files_list

    def load_txt_data(self, file):
        with open(file, 'r', encoding='utf-8') as f:
            data = f.read()
            return data

    def get_text(self, product):
        '''
        получить шаблон текста конкретного товара
        :param product:
        :return:
        '''
        if len(self.product_texts[product]) == 0:
            self.product_texts[product] = self.load_product_text(product)
        cur_txt = self.product_texts[product].pop()
        return cur_txt





