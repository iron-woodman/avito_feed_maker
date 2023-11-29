
def read_data(file):
    colors = []
    with open (file, 'r', encoding='utf-8') as f:
        colors = f.read().split('\n')
        return colors



length = [l for l in range(100, 305, 5)]
width = [w for w in range(45, 71, 1)]
colors = read_data('colors.txt')

set_length = set(length)
set_width = set(width)
set_colors = set(colors)



print(set_length)
print(set_width)
print(set_colors)