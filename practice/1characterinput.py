name = input("What is you name? :")
age = int(input("How old are you? :"))
year = int(input("What year do you live in? :"))
hundred = year - age + 100
copies = int(input("How many copies of this message would you like? :"))
message = name + ", you will be 100 years old in " + str(hundred)
for i in range(copies):
    print(message)
