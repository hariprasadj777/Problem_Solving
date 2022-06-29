"""There is a horizontal row of  cubes. The length of each cube is given. 
You need to create a new vertical pile of cubes. 
When stacking the cubes, you can only pick up either the leftmost or the rightmost cube each time. 
Print Yes if it is possible to stack the cubes. Otherwise, print No.

Input Format:
The first line contains a single integer , the number of test cases.
For each test case, there are  lines.
The first line of each test case contains , the number of cubes.
The second line contains  space separated integers, denoting the sideLengths of each cube in that order"""

n = int(input())
for i in range (n):
    blocks = list(map(int,input("\nEnter the numbers : ").strip().split()))
    a=max(blocks)+1
    b=min(blocks)
    for j in range(len(blocks)):
        x = max(blocks[0],blocks[-1])
        if  bool(b!=x) & bool(a >= x):
            a=x
            blocks.remove(x)
        elif b == x:
            print("YES")
            break
        else:
            print("NO")
            break  