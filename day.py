items = ["misc", "phone", 323.23, 3212.222, "Justin", "bag", "Cliff bars", 134]

str_items = []
num_items = []

for i in items:
    if isinstance(i, float) or isinstance(i, int):
        num_items.append(i)
    elif isinstance(i, str):
        str_items.append(i)
    else:
        pass
        
print(str_items)
print(num_items)


def parse_lists(some_list):
    str_list_items = []
    num_list_items = []
    for i in some_list:
        if isinstance(i, float) or isinstance(i, int):
            num_list_items.append(i)
        elif isinstance(i, str):
            str_list_items.append(i)
        else:
            pass
    return str_list_items, num_list_items

    print(parse_lists(items))


def my_sum(my_sum_list):
    