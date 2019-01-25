
print("1 * 1 : %d" % 1*1)

dan = 1
for i in range(1,10):
    print("%d * %d : %d" % (dan, i, dan * i))


for dan in range(1,10):
    for i in range(1,10):
        print("%d * %d : %d" % (dan, i, dan * i))
