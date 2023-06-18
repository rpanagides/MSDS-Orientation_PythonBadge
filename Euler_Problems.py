import matplotlib
import numpy as np
import pandas as pd

#Problem 1:

multiple_sum = 0

for i in range(1000):
    if i % 3 == 0 or i % 5 == 0:
        if i % 3 == 0:
            multiple_sum += i
        elif i % 5 == 0:
            multiple_sum += i

#print(multiple_sum)

#Problem 2:

evensum = 2

a = 1
b = 2
c = 0

while c < 4000000:
    if c % 2 == 0:
        evensum += c
    c = a + b
    a = b
    b = c

#print(evensum)

#Problem 3:

x = 600851475143
n = 3

while n < x/2:
    if x % n == 0:
        x = x / n
        print(x)
    n += 1

print(x) 
