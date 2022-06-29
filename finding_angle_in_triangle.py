"""In a right angle triangle ABC, point M is the midpoint of the hypotenues AC.
You are given the length of AB and BC.
Find the angel MBC"""

from math import sqrt
import math
ab = int(input())
bc = int(input())
cm = (sqrt((ab**2)+(bc**2)))/2
bn = bc/2
angle = round(math.degrees(math.acos(bn/cm)))
print(str(angle)+chr(176))




