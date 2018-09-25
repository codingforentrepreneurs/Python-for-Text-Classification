
bow = []


def make_bag(new_item=None):
    global bow
    new_item_list = []
    if new_item is not None:
        if isinstance(new_item, list):
            new_item_list = new_item
        if isinstance(new_item, str):
            new_item_list = [x for x in new_item.split()]
    for item in new_item_list:
        final_item = item.lower().strip()
        if final_item not in bow:
            bow.append(final_item)
    return bow

def to_one_hot(text, add_to_bag=True, bow=None):
    if bow is not None:
        current_bow = bow
    else:
        if add_to_bag:
            current_bow = make_bag(text)
        else:
            current_bow = make_bag(new_item=None)
    text_list = []
    if isinstance(text, list):
        text_list = new_item
    if isinstance(text, str):
        text_list = [x for x in text.split()]
    oha = []
    i = 0 # position of current bow iteration
    for word in current_bow:
        oha.append(0)
        for item in text_list:
            if item.lower().strip() == word:
                oha[i] = 1
        i += 1
    return oha

def oha_to_text(oha_array):
    current_bow = make_bag()
    sent = ''
    i = 0
    for pos in oha_array: # [1,0,1]
        if pos == 1:
            sent += " " + current_bow[i]
        i += 1
    return sent.strip()


def clean_line(line):
    escaped = ""
    for word in line.replace("\n", "").split():
        word = word.replace(".", " ")
        word = word.replace(",", " ")
        word = word.replace("?", " ")
        word = word.replace("!", " ")
        word = word.replace(":", " ")
        word = word.replace("'", " ")
        word = word.replace("\"", " ")
        word = word.replace(")", " ")
        word = word.replace("(", " ")
        word = word.replace("[", " ")
        word = word.replace("]", " ")
        word = word.replace(";", " ")
        word = word.replace("&", " ")
        word = word.replace("-", " ")
        word = word.replace("*", " ")
        word = word.replace("=", " ")
        word = word.replace("/", " ")
        word = word.replace("\\", " ")
        word = word.replace("'s", " is")
        word = word.replace("'m", " am")
        word = word.replace("'ll", " will")
        word = word.replace("n't", " not")
        word = word.replace("@", "")
        word = word.strip()
        escaped += " " + word
    return escaped.strip()



