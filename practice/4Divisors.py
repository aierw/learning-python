num = int(input("Enter a number: "))
divisors = []
for x in range(1, num+1):
    if num % x == 0:
        divisors.append(x)
print(f"Divisors are: {divisors}")