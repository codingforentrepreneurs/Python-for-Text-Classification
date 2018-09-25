import csv
import os


ROOT_DIR = os.getcwd()
RAW_PATH = os.path.join(ROOT_DIR, 
        'raw_src', 
        'smsspamcollection', 
        'SMSSpamCollection')

NOT_SPAM_TXT = os.path.join(ROOT_DIR, 'not-spam.txt')
SPAM_TXT = os.path.join(ROOT_DIR, 'spam.txt')

not_spam_file = open(NOT_SPAM_TXT, 'w')
spam_file = open(SPAM_TXT, 'w')
with open(RAW_PATH, 'r') as f:
    lines = f.readlines()
    for line in lines:
        label, txt = line.split('\t')
        print(label, txt)
        if label == 'ham':
            not_spam_file.write(txt)
        if label == 'spam':
            spam_file.write(txt)

not_spam_file.close()
spam_file.close()



