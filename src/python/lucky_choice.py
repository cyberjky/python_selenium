import random

#case1
result = []
bonus = []
numberbox = set(range(1,46))

for i in range(7):
    temp = random.choice(list(numberbox))
    if i < 6:
        result.append(temp)
    else:
        bonus.append(temp)

    numberbox.remove(temp)

result.sort()
print("result : ", *result)
print("bonus : ", *bonus)


#case2
s = random.sample(numberbox, 7)
s.sort()
print(s)

