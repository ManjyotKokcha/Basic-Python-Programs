import numbers


number = int(input("Enter number:"))
print(f"Before reverse:{number}")
reverse = 0
while number != 0:
    reverse = reverse*10 + number % 10
    number = (number//10)


print(f"After reverse:{reverse}")
