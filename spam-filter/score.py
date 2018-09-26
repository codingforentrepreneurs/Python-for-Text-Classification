# 1. new data or data the clf hasn't seen
# 2. test data has the same amount for each label

import os
import numpy as np
from predict import predict
from sklearn.metrics import accuracy_score


bag = []

ROOT_DIR            = os.getcwd()
SPAM_DATA_PATH      = os.path.join(ROOT_DIR, 'data', 'spam', 'spam.txt')
NOT_SPAM_DATA_PATH  = os.path.join(ROOT_DIR, 'data', 'spam', 'not-spam.txt')
SPAM_LABEL          = 0
NOT_SPAM_LABEL      = 1

MAX_LINES = 500
MAX_TEST_LINES = 747

y_pred = []
y_true = []


def run_analysis(filepath=SPAM_DATA_PATH, label=SPAM_LABEL):
    with open(filepath, 'r') as f:
        lines = f.readlines()[MAX_LINES:MAX_TEST_LINES] #same amount of data
        for line in lines:
            y_true.append(label)
            pred_label = predict(line)[0]
            y_pred.append(pred_label)


run_analysis(filepath=SPAM_DATA_PATH, label=SPAM_LABEL)
run_analysis(filepath=NOT_SPAM_DATA_PATH, label=NOT_SPAM_LABEL)


score = accuracy_score(y_true, y_pred)

print(score)






