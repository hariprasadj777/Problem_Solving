"""Designer WELCOME mat
Enter the dimensions such that N is a odd number and M is 3 times the value of N"""

n = int(input("Enter the value of N"))
m = int(input("Enter the value of M"))
a=""
for i in range(1,n,2):
    o=(m-3*i)/2
    round(o)
    for j in range(int(o)):
        a=a+"-"
    for k in range(i):
        a=a+".|."
    for l in range(int(o)):
        a=a+"-"
    print(a)
    a=""
p=(m-7)/2
for i in range(int(p)):
    a=a+"-"
a=a+"WELCOME"
for i in range(int(p)):
    a=a+"-"
print(a)
a=""
for i in range(n-2,0,-2):
    o=(m-3*i)/2
    round(o)
    for j in range(int(o)):
        a=a+"-"
    for k in range(i):
        a=a+".|."
    for l in range(int(o)):
        a=a+"-"
    print(a)
    a=""
