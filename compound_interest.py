def comp_interest(p, r, t):
    print("Principal: ", p)
    print("Rate:", r)
    print("Time:", t)

    a = p * pow((1 - r/100), t)
    ci = a - p
    return ci


p = int(input("Enter pricipal:"))
r = int(input("Enter rate:"))
t = int(input("Enter time:"))

compound = comp_interest(p, r, t)

print(f"Compound interest is {compound}")
