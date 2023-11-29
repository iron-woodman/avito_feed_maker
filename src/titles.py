import random

class Title:
    stol_titles = []
    um_titles = []
    podokonnik_titles = []

    def __init__(self):
        self.stol_titles = self.load_titles('titles/stol.txt')
        self.um_titles = self.load_titles('titles/um.txt')
        self.podokonnik_titles = self.load_titles('titles/podokonnik.txt')

    def get_um_title(self):
        """
        получить заголовок для умывальника
        :return:
        """
        return random.choice(self.um_titles)

    def get_pod_title(self):
        """
        получить заголовок для подоконника
        :return:
        """
        return random.choice(self.podokonnik_titles)

    def get_stol_title(self):
        """
        получить заголовок для столешницы
        :return:
        """
        return random.choice(self.stol_titles)


    def load_titles(self, file):
        with open(file, 'r', encoding='utf-8') as f:
            return f.read().split('\n')