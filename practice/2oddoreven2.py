number = int(input("Give me the number: "))
if number % 2 == 0:
    print(f"{number} - even number")
else:
    print(f"{number} - odd number")
if number % 4 == 0:
    print("And is also a multiply of 4")

num = int(input("Give me a divider: "))
check = int(input("Gve me a dividend: "))
if num % check == 0:
    print(f"{check} divides evenly into {num}")
else:
    print(f"{check} does not dicides evenly into {num}")