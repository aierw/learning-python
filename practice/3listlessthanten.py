#a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#for x in a:
    #if x<=5: print(x)

#print( [ x for x in a if x<5])

numbers = [1, 3, 2, 24, 2, 56, 6, 3, 45, 8, 24, 4, 12, 95, 23, 65, 101, 43]
lessAnums = []
lessBnums = []

for num in numbers:
    if num <= 5:
        lessAnums.append(num)
        lessAnums.sort()
       

print(lessAnums)
print()

num = int(input("Enter a number: "))
for n in numbers:
    if n <= num:
        lessBnums.append(n)
        lessBnums.sort()

print(lessBnums)


