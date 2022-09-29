import paragraph as paragraph

print(((500//7) % 5) ** 3)

S = 'I love Python'
print(S[2:5])
print(S[2:6])
print(S[3:7])
print(S[-11:-7])
print(S[-11:-8])
print(3 * 3 ** 3)

#Tuple

T = (3, 5, 7, 11)
l1 = list(T)
l1.append(9)
print(l1)
print(T)

L1 = ['Vikas', 'Akshay', 'Sanskar', 'Mahima']
print(L1[1][-1])

l = [32, 34, 12, 27, 33]
l.append([14, 19])
print(len(l))

print("Dic")
D = {1:['Raj', 22], 2:['Simran', 21], 3:['Rahul', 40]}
for val in D:
     print(val)

# 6

# for sentence in paragraph:
#     for word in sentence.split():
#         single_word_list.append(word)


print(list(range(10, 1, -1)))

# Coding exercise 1

C = [7, 8, 9, 18, 20, 21, 25, 26, 27, 31, 32, 34, 35, 36, 40, 43, 45, 47, 53, 58, 62, 67, 68, 71, 72, 74, 75, 76, 80, 81, 82, 90, 93, 95, 97, 99]
F = [1, 7, 10, 13, 16, 22, 24, 29, 30, 32, 34, 39, 40, 43, 44, 48, 56, 60, 65, 68, 69, 73, 77, 78, 90, 93, 94, 95, 96]
H = [5, 12, 14, 17, 20, 21, 22, 25, 28, 30, 37, 38, 39, 40, 42, 44, 57, 59, 61, 62, 67, 71, 75, 76, 77, 82, 83, 86, 87, 92, 94, 95]
