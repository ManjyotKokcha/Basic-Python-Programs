def prime(x, y):
    prime_list = []
    for i in range(x, y):
        if i == 0 or i == 1:
            continue
        else:
            for j in range(2, int(i/2)+i):
                if i % j == 0:
                    break
                else:
                    prime_list.append(i)
    return prime_list


start_range = int(input("Enter Start range: "))
end_range = int(input("Enter End range: "))

lst = prime(start_range, end_range)
if len(lst) == 0:
    print("No Prime numbers found")
else:
    print("List of prime numbers are: ", lst)
