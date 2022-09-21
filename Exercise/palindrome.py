s = "malayalam"
#s = input()
rever = s[::-1]
print(rever)
if s == rever:
    print("True")
else:
    print("False")

s1 = 'hello'
s1 = s1[::-1]
print(s1)

str = "I love coding"
ss = str.split(' ')
print(ss)
reverse_str = ' '.join(reversed(ss))
print(reverse_str)

def reverseWords(s):
    words = s.split(' ')
    reverse_str = ' '.join(reversed(words))
    return reverse_str

s1 = "I love Programming"
print (reverseWords(s1))

import stringcase

s = "I love proGramming"
st = stringcase.titlecase(s)
print(st)

list1 = [23, 45, 34]
import numpy as np
lst = np.array(list1)
print(type(lst))
print(lst)


import statistics as stat
lr = stat.LinearRegression()

import logging

import pandas as pd
pd