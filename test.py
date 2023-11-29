import itertools
import random


def interleave_lists(list1, list2):
    # itertools.zip_longest fills missing values with None, allowing to interleave lists of different lengths
    merged = list(itertools.chain(*itertools.zip_longest(list1, list2)))
    # Filter out any None values that may have been added
    merged = [item for item in merged if item is not None]
    return merged


def union_lists(list1: list, list2: list) -> list:
    res_list=[]
    big_list = []
    small_set = set()

    if len(list1) > len(list2):
        proportion = int(len(list1) / len(list2))
        small_set = set(list2)
        big_list = list1
    else:
        proportion = int(len(list2) / len(list1))
        small_set = set(list1)
        big_list = list2

    big_list_elements_counter = 0
    for item in big_list:
        res_list.append(item)
        big_list_elements_counter += 1
        if big_list_elements_counter == proportion:
            if len(small_set) > 0:
                res_list.append(small_set.pop())
            big_list_elements_counter = 0

    while len(small_set) > 0:
        res_list.insert(random.randint(0, len(res_list)), small_set.pop())

    return res_list


# Example usage
list2 = [1, 2, 3, 4, 5, 6,7, 8]
list1 = ['a', 'b', 'c', 'd', 'e', 'g', 'f','q', 'w', 'r', 'h']
merged = union_lists(list1, list2)
print(merged)
print(len(list1), len(list2), len(merged))