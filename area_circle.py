def area(r):
    print("Enter radius: ", r)

    area = 3.14 * pow(r, 2)
    return area


r = int(input("Enter radius: "))
a = area(r)

print("Area of circle", a)
