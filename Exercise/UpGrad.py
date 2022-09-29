# 1. No Spaces
s = 'Data Science'
s = s.lower()
words = s.split(' ')
final_list = [word[0].upper() + word[1:] for word in words]
final_string = '_'.join(final_list)
print(final_string)

# 2. Move Vowels

sv = 'You love Python!'
vowels = 'aeiouAEIOU'
v = ''
o = ''

for i in sv:
    if i in vowels:
        v = v + i
    else:
        o = o + i
final_string_v = v + o
print(final_string_v)

# 3. Common Prefix

print("Common Prefix - Started")
string1 = 'upgradData'
string2 = 'upGradScience'

string1 = string1.lower()
string2 = string2.lower()

l1 = len(string1)
l2 = len(string2)

min_len = min(l1, l2)

for i in range(min_len):
    if string1[i] != string2[i]:
        break
if i == 0:
    print(-1)
else:
    print(string1[:i])

# 4.anagrams
print('anagrams')
s1 = 'upgrad'
s2 = 'found'


def anagram(s1, s2):
    if len(s1) != len(s2):
        return False
    for i in range(len(s1)):
        if s1.count(s1[i]) != s2.count(s1[i]):
            return False
    return True


print(anagram(s1, s2))

# 5 Remove duplicates

# input - [4, 4, 4, 4]

import ast

mylist = ast.literal_eval(input())

d = {}
for item in mylist:
    if item not in d:
        d[item] = 1
print(list(d.keys()))

# Dic and list
print("Dic and list")
final_list1 = []
input_dict = {'Mobile': ['Redmi', 'Samsung', 'Realme'], 'Laptop': ['Dell', 'HP'], 'TV': ['Videocon', 'Sony']}
for key in input_dict.keys():
    for word in input_dict[key]:
        final_list1.append(str(key + '_' + str(word)))
print(final_list1)

# UpGrad String

s = 'ab#ab#aba'
d = {}
for i in s:
    if i not in d:
        d[i] = 1
    else:
        d[i] = d[i] + 1
vals = d.values()
n = len(d)


def upgrad_string(vals):
    for i in range(1, n + 1):
        if i not in vals:
            return False
    return True


print(upgrad_string((vals)))


# Balanced Brackets

inp = '){[[]]}())()'

stack = []
for i in inp:
    if len(stack) == 0:
        stack.append(i)
    else:
        if i == ')' and stack[-1] == '(':
            stack.pop()
        elif i == '}' and stack[-1] == '{':
            stack.pop()
        elif i == ']' and stack[-1] == '[':
            stack.pop()
        else:
            stack.append(i)
if stack:
    print('No')
else:
    print('Yes')
