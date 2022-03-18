
# for x raise to y
# def power(x, y):
#     if y == 0:
#         return 1
#     if y % 2 == 0:
#         return pow(x, y//2) * pow(x, y//2)
#     return pow(x, y//2) * pow(x, y//2)

# for order


def order(x):
    n = 0
    while(x != 0):
        n = n + 1
        x = x//10
    return n

# Armstrong


def armstrong(x):

    n = order(x)
    temp = x
    sum1 = 0

    while (temp != 0):
        r = temp % 10
        sum1 = sum1 + pow(r, n)
        temp = temp//10
    return (sum1 == x)


a = int(input("Enter number: "))

arm = armstrong(a)

print(f"Armstrong = ", arm)
