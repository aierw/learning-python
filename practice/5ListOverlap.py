import random
min = 1
max = 20
quantity = 10
list1 = [random.randint(min, max) for _ in range(quantity)]
list2 = [random.randint(min, max) for _ in range(quantity)]
print(list1)
print(list2)
same_num = []
for num in list1:
    if num in list2 and num not in same_num:
        same_num.append(num)
print(same_num)
