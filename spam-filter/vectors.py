import os
import numpy as np
from preprocessing import make_bag, to_one_hot, oha_to_text, clean_line
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences
from keras.utils import to_categorical

from sklearn.preprocessing import LabelEncoder


bag = []

ROOT_DIR            = os.getcwd()
SPAM_DATA_PATH      = os.path.join(ROOT_DIR, 'data', 'spam', 'spam.txt')
NOT_SPAM_DATA_PATH  = os.path.join(ROOT_DIR, 'data', 'spam', 'not-spam.txt')
MAX_LINES           = 500
MAX_NUM_WORDS       = 20000
MAX_SEQUENCE_LENGTH = 1000 # important 


def split_textfiles(paths=[], limit=10000):
    texts = []
    labels = []
    for path in paths:
        with open(path, 'r') as f:
            filename = os.path.basename(path) # f.name
            label, ext = os.path.splitext(filename)
            lines = f.readlines()[:limit]
            for line in lines:
                # clean line text
                texts.append(line)
                labels.append(label)
    return texts, labels


texts, labels = split_textfiles(paths=[
        SPAM_DATA_PATH,
        NOT_SPAM_DATA_PATH,
], limit=10000)



tokenizer = Tokenizer(num_words=MAX_NUM_WORDS)
tokenizer.fit_on_texts(texts)
sequences = tokenizer.texts_to_sequences(texts)
data = pad_sequences(sequences, maxlen=MAX_SEQUENCE_LENGTH)
encoder = LabelEncoder()
encoder.fit(labels)
encoded_Y = encoder.transform(labels)

y = to_categorical(encoded_Y)

print(data, y)

X = data # training data X[0] = y[0] # spam, X[1]  = y[1] # spam
y = y # labels

# from sklearn.model_selection import train_test_split

# X_train, X_test, y_train, y_test = train_test_split(
#     X, y, test_size=0.33, random_state=42)

print(X.shape)
indices = np.arange(X.shape[0])
print(indices)
np.random.shuffle(indices)
print(indices)

X = X[indices]
y = y[indices]

num_samples = 0.33 * X.shape[0]

X_train = X[:-num_samples] # 67%
X_test = X[-num_samples:] # 33%
y_train = y[:-num_samples] # 67%
y_test = y[-num_samples:] # 33%









