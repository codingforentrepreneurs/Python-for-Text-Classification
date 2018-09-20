
bow = []

def make_bag(new_item):
    global bow
    new_item_list = []
    if isinstance(new_item, list):
        new_item_list = new_item
    if isinstance(new_item, str):
        new_item_list = [x for x in new_item.split()]
    for item in new_item_list:
        final_item = item.lower().strip()
        if final_item not in bow:
            bow.append(final_item)
    return bow
