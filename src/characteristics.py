import os


class Characteristics:
    length = set()
    width = set()
    colors = set()

    def __init__(self, colors_file: str):
        self.colors_file = colors_file


    def load_colors(self):
        with open(self.colors_file, 'r', encoding='utf-8') as f:
            self.colors = set(f.read().split('\n'))

    def get_color(self):
        '''
        получить цвет
        :param product:
        :return:
        '''
        if len(self.colors) == 0:
            self.load_colors()
        cur_color = self.colors.pop()
        return cur_color

    def get_width(self):
        '''
        получить ширину
        :param product:
        :return:
        '''
        if len(self.width) == 0:
            self.width = set([w for w in range(45, 71, 1)])
        cur_width = self.width.pop()
        return cur_width


    def get_length(self):
        '''
        получить длину
        :param product:
        :return:
        '''
        if len(self.length) == 0:
            self.length = set([l for l in range(100, 305, 5)])
        cur_length = self.length.pop()
        return cur_length

    def get_full_row(self):
        return f'Характеристики:\n- Длина: {self.get_length()} см.\n- Ширина: {self.get_width()} см. \n- Цвет: {self.get_color()}'
