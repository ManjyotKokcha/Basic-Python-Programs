
from ast import Break

i, temp = 0, 0
n = int(input("Enter number:"))


for i in range(2, n):
    if n % i == 0:
        temp = 1
        Break
if temp == 1:
    print("not a prime number")
else:
    print("Prime number")
