bow = []

def make_bag(new_item):
    global bow
    new_item_list = []
    if isinstance(new_item, list): 
        new_item_list = new_item   
    if isinstance(new_item, str):
        new_item_list = [x.lower().strip() for x in new_item.split()]
    for item in new_item_list:
        if item not in bow:
            bow.append(item)