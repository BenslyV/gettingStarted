import ast
mylist = ast.literal_eval(input())
m = mylist[0]
n = mylist[1]
# print(m)
# print(n)

final = [0]*n

final = [list(final) for i in range(m)]

for i in range(m):
	for j in range(m):
		if i==0 or j==0 or i==m-1 or j==n-1:
			final[i][j] = 1
for i in final:
	print(i)

