#To find whehter a given number is a prime number
num = int(input("Enter the number to check whehter it is a prime number:" ))
flag = False
if num > 1:
    # check for factors
    for i in range(2, num):
        if (num % i) == 0:
            flag = True
            break
if flag:
    print("NOt a prime number")
else:
    print("Is a prime number")