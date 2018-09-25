import numpy as np
from preprocessing import make_bag, to_one_hot, oha_to_text

import pickle

clf = pickle.load(open('data/pickles/classifier.pkl', 'rb'))

def predict(txt):
    oha_txt             = to_one_hot(txt, add_to_bag=False)
    prediction_array    = np.array(oha_txt)
    return clf.predict([prediction_array]) # 1 or 0

print(predict("bad one")) # 0
print(predict("great and good")) # 1 
print(predict("that was just an incredible movie.")) # 
















