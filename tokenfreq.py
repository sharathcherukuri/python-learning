import re
import nltk
import json
def f2string(fname):
    with open(fname,'r') as f:
        return f.read()
def tokenfreq():
    s= f2string('us_constitution.txt')
    toks=nltk.word_tokenize(s)
    s2 = []
    for i in toks:
        if i not in s2:
            s2.append(i)
    for i in range(0,len(s2)):
        


