# take the input here
number = int(input())


# the function definition starts here
def factorial(n):
    # write the funtion here that finds and RETURNS factorial of next
    fact = 1

    if n < 0:
        return -1
    elif n == 0:
        return 1
    else:
        for i in range(1, n + 1):
            fact = fact * i

        # print ("The factorial of 23 is : ",end="")
        # print (fact)
        return fact


# function definition ends here

# do not alter the code typed below
k1 = factorial(number)
print(k1)

L = [2, 3, 4, 2, 1, 2, 3]
print(f"printing index  {L.index(2)}")

print("printing k")
L = [2, 1, 2, 4, 5, 3, 6]
K = 4 in L
print(K)

