import numpy as np
from preprocessing import make_bag, to_one_hot, oha_to_text, clean_line

import pickle

clf = pickle.load(open('data/pickles/classifier.pkl', 'rb'))
bow = pickle.load(open('data/pickles/bow.pkl', 'rb'))

def predict(txt):
    txt                 = clean_line(txt)
    oha_txt             = to_one_hot(txt, add_to_bag=False, bow=bow)
    prediction_array    = np.array(oha_txt)
    return clf.predict([prediction_array]) # 1 or 0


'''
1 - Not Spam
0 - Spam
'''
# print(predict("bad one")) # [1]
# print(predict("great and good")) # 1 
# print(predict("that was just an incredible movie.")) #1
# print(predict("Had your contract mobile 11 Mnths? Latest Motorola, Nokia etc. all FREE! Double Mins & Text on Orange tariffs. TEXT YES for callback, no to remove from records.")) #0 
# print(predict("PRIVATE! Your 2003 Account Statement for 07808247860 shows 800 un-redeemed S. I. M. points. Call 08719899229 Identifier Code: 40411 Expires 06/11/04")) #0
# print(predict("SMS SERVICES. for your inclusive text credits, pls goto www.comuk.net login= 3qxj9 unsubscribe with STOP, no extra charge. help 08702840625.COMUK. 220-CM2 9AE")) #0














