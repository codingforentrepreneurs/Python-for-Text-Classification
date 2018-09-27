import os
from preprocessing import make_bag, to_one_hot, oha_to_text, clean_line
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences
from keras.utils import to_categorical

bag = []

ROOT_DIR            = os.getcwd()
SPAM_DATA_PATH      = os.path.join(ROOT_DIR, 'data', 'spam', 'spam.txt')
NOT_SPAM_DATA_PATH  = os.path.join(ROOT_DIR, 'data', 'spam', 'not-spam.txt')
SPAM_LABEL          = 0
NOT_SPAM_LABEL      = 1
MAX_LINES           = 500
MAX_NUM_WORDS       = 1000
MAX_SEQUENCE_LENGTH = 10

texts = ["this is awesome", "this is not great", "this is cool!"]
tokenizer = Tokenizer(num_words=MAX_NUM_WORDS)
tokenizer.fit_on_texts(texts)

'''
print(tokenizer.document_count)
print(tokenizer.num_words)
print(tokenizer.word_counts)
print(tokenizer.word_docs)
print(tokenizer.word_index)

{'this': 1, 'is': 2, 'awesome': 3, 'not': 4, 'great': 5, 'cool': 6}
'''

sequences = tokenizer.texts_to_sequences(texts)

'''
print(sequences)

[[1, 2, 3], [1, 2, 4, 5], [1, 2, 6]]


[1, 2, 3]
[1, 2, 4, 5]
[1, 2, 6]
'''
data = pad_sequences(sequences, maxlen=MAX_SEQUENCE_LENGTH)

print(data)






