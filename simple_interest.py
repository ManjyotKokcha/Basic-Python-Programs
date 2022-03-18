def simple_interest(p, n, r):
    print(" principle: ", p)
    print(" number of years: ", n)
    print(" rate: ", r)

    si = (p * n * r)/100
    return si


p = int(input("Enter P: "))
n = int(input("Enter n:"))
r = int(input("Enter r:"))

s1 = simple_interest(p, n, r)
print("Simple interest is ", s1)
