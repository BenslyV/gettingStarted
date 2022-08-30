import ast,sys
input_str = 'alpha'

#Write your code here
#Use capital YES or NO
vowels = ('a','e','i','o','u','A','E','I','O','U')
vowel_or_not = input_str.startswith(vowels)
print(type(vowel_or_not))
print(vowel_or_not)

if vowel_or_not==True:
    print("Vowel")
else:
    print("Not a Vowel")

# Exercise 2 - Output in Title Case

input_str = ['VARMA', 'raj', 'Gupta', 'SaNdeeP']
input_str = str(input_str)
print(type(input_str))

#
# def capitalizeWords(input_str):
#   return input_str.sub(r'\w+', lambda m:m.group(0).capitalize(), s)
#
# capitalizeWords(input_str)
# print(input_str)

import stringcase
title_case = stringcase.camelcase(input_str)
print(title_case)

