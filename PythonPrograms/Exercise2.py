list = [50, 60, 49]
print(list)
print(type(list))
list.append(46)
print(list)
#you have to take input on your own here



#write your code here

#Take input here
#we will take input using ast sys
import ast
input_str = input()
input_list = ast.literal_eval(input_str)

def average(lst):
    sum_of_list = 0
    for i in range(len(lst)):
        sum_of_list += lst[i]
    average = sum_of_list/len(lst)
    return average

#Remember how we took input in the Alarm clock Question in previous Session?
#Lets see if you can finish taking input on your own

data=input_list[0]
check=input_list[1]
# print(data)
# print(check)
avg = int(average(data))

#start writing your code to find if check is above average of data
for x in check:
    if x>avg:
        data.append(x)
print(data)

for x in check:
    if x > avg:
        data.append(x)
        new_avg = int(average(data))

        if new_avg < avg:
            data.pop(-1)

print(data)






