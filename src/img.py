import os


class Img:

    product_img_url = dict() # key=product, value= dict(key='photo_number' value = set{url_photo1, url_photo1})

    def __init__(self, company_name:str, products: list, img_count:int):
        self.company_name = company_name
        self.products = products
        self.img_count_per_add = img_count
        self.load_all_img_urls()


    def load_url_set(self, file):
        with open(file, 'r', encoding='utf-8') as f:
            data = set(f.read().split('\n'))
            return data


    def load_all_img_urls(self):
        """
        загрузить список всех текстов по всем категориям товаров (столешницы, умывальники, подоконники)
        :return:
        """
        for product in self.products:
            self.product_img_url[product] = dict()
            for img_number in range(1, self.img_count_per_add+1):
                self.product_img_url[product][img_number] = self.load_product_urls(product, img_number)




    def load_product_urls(self, product_name: str, img_number: int) -> set:
        file = f'company/{self.company_name}/IMG_URLS/{product_name}/img{img_number}_urls.txt'
        url_set = self.load_url_set(file)
        return url_set




    def get_url(self, product: str, img_number: int) -> str:
        '''
        получить шаблон текста конкретного товара
        :param product:
        :return:
        '''
        if len(self.product_img_url[product][img_number]) == 0:
            self.product_img_url[product][img_number] = self.load_product_urls(product, img_number)
        cur_url = self.product_img_url[product][img_number].pop()
        return cur_url