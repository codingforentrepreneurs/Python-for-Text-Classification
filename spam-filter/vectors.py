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


texts = ["this is awesome", "this is not great", "this is cool!"]
tokenizer = Tokenizer(num_words=MAX_NUM_WORDS)
tokenizer.fit_on_texts(texts)

#print(dir(tokenizer))

print(tokenizer.document_count)
print(tokenizer.num_words)
print(tokenizer.word_counts)
print(tokenizer.word_docs)
print(tokenizer.word_index)





sequences = tokenizer.texts_to_sequences(texts)

#print(sequences)

