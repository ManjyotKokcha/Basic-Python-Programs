# import math

# n = input("Enter a number: ")

# f = math.factorial(int(n))

# print(f"Factorial = {f}")


def fact(n):
    if n < 0:
        return 0
    elif n == 0 or n == 1:
        return 1
    else:
        f = 1
        while (n > 1):
            f *= n
            n -= 1
        return f


num = int(input("Enter number: "))

print("factorial of", num, " is ", fact(num))
