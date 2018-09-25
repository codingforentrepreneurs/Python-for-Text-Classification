import os
from preprocessing import make_bag, to_one_hot, oha_to_text, clean_line


bag = []

ROOT_DIR            = os.getcwd()
SPAM_DATA_PATH      = os.path.join(ROOT_DIR, 'data', 'spam', 'spam.txt')
NOT_SPAM_DATA_PATH  = os.path.join(ROOT_DIR, 'data', 'spam', 'not-spam.txt')
SPAM_LABEL          = 0
NOT_SPAM_LABEL      = 1

MAX_LINES = 500

def file_to_bow(filepath=NOT_SPAM_DATA_PATH):
    global bag
    with open(filepath, 'r') as f:
        lines = f.readlines()[:MAX_LINES]
        for line in lines:
            escaped_line = clean_line(line)
            bag = make_bag(escaped_line)


file_to_bow(filepath=NOT_SPAM_DATA_PATH)
file_to_bow(filepath=SPAM_DATA_PATH)



#print(bag)

'''
Positive = label = 1
Negative = label = 0

'''

def file_to_oha(filepath=NOT_SPAM_DATA_PATH, label=1):
    my_oha = []
    labels = []
    with open(filepath, 'r') as f:
        lines = f.readlines()[:MAX_LINES]
        for line in lines:
            escaped_line = clean_line(line)
            oha = to_one_hot(escaped_line)
            labels.append(label)
            my_oha.append(oha)
    return my_oha, labels




pos_ohas, pos_labels = file_to_oha(filepath=NOT_SPAM_DATA_PATH, label=NOT_SPAM_LABEL)
neg_ohas, neg_labels = file_to_oha(filepath=SPAM_DATA_PATH, label=SPAM_LABEL)


#print(pos_ohas, pos_labels)

import numpy as np
X_pos = np.array(pos_ohas)
X_neg = np.array(neg_ohas)

y_pos = np.array(pos_labels)
y_neg = np.array(neg_labels)

X = np.concatenate((X_pos, X_neg), axis=0)
y = np.concatenate((y_pos, y_neg), axis=0)


#X = Training data
#y = labels = target = this actual value of that trainin data

print(X)
print(y)
# print(len(X) == 14)
# print(len(y) == len(X))

from sklearn.utils import shuffle

X, y = shuffle(X, y, random_state=0)


#print(X)
#print(y)

from sklearn import svm
clf = svm.SVC()
clf.fit(X, y)

#clf.predict([[2., 2.]])
import pickle

pickle.dump(clf, open('data/pickles/classifier.pkl', 'wb'))
pickle.dump(bag, open('data/pickles/bow.pkl', 'wb'))









