# -*- coding: utf-8 -*-
from snownlp import SnowNLP
import codecs
import os

source = open("004.txt", "r", encoding='utf-8')
line = source.readlines()
pos = 0
neg = 0
mut = 0
sentimentslist = []
for i in line:
    s = SnowNLP(i)
    print(s.sentiments)
    if s.sentiments > 0.6:
        pos += 1
    elif s.sentiments < 0.4:
        neg += 1
    else:
        mut += 1
    sentimentslist.append(s.sentiments)

import matplotlib.pyplot as plt
import numpy as np

plt.hist(sentimentslist, bins=np.arange(0, 1, 0.01), facecolor='g')
plt.xlabel('Sentiments Probability')
plt.ylabel('Quantity')
plt.title('picture 004')
plt.show()
print(pos)
print(neg)
print(mut)