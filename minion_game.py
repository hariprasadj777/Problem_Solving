"""Kevin and Stuart want to play the 'The Minion Game'.

Game Rules:

Both players are given the same string, .
Both players have to make substrings using the letters of the string .
Stuart has to make words starting with consonants.
Kevin has to make words starting with vowels.
The game ends when both players have made all possible substrings.

Scoring:
A player gets +1 point for each occurrence of the substring in the string .

Output:
The winner's name and score, separated by a space on one line, or Draw if there is no winner
"""



a = input()
b = len(a)
vowels = ("a","e","i","o","u")
answer1 = []
answer2 = []
def kevin():
    c=a[i]
    answer1.append(c)
    for j in range(i+1,b):
        c=c+a[j]
        answer1.append(c)
def stuart():
    c=a[i]
    answer2.append(c)
    for j in range(i+1,b):
        c=c+a[j]
        answer2.append(c)
for i in range(b):
    if (a[i] in vowels)==True:
        kevin()
    else:
        stuart()
p = len(answer1)
q = len(answer2)
if p>q:
    print("Kevin "+str(p))
elif q>p:
    print("Stuart "+str(q))
elif p==q:
    print("Draw")
print(answer1)
print(answer2)