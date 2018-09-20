from preprocessing import make_bag, to_one_hot, oha_to_text


bag = []


def file_to_bow(filepath='data/simple/pos.txt'):
    global bag
    with open(filepath, 'r') as f:
        lines = f.readlines()
        for line in lines:
            escaped_line = line.replace('\n', '')
            bag = make_bag(escaped_line)


file_to_bow(filepath='data/simple/pos.txt')
file_to_bow(filepath='data/simple/neg.txt')



print(bag)
