from functools import reduce

# case1
a = 1
b = 2
c = 3
d = 4
e = 5
f = 6
g = 7
h = 8
i = 9
j = 10
k = a + b + c + d + e + f + g + h + i + j
print('case1', k)

# case2
a = 1
b = 2
c = 3
d = 4
e = 5
f = 6
g = 7
h = 8
i = 9
j = 10
print('case2', a + b + c + d + e + f + g + h + i + j)

# case3
case3_total = 0
for i in range(10):
    case3_total = case3_total + (i + 1)
print('case3', case3_total)

# case4-1
case4_total = 0
for i in range(11):
    case4_total = case4_total + i
print('case4-1', case4_total)

# case4-2
case4_total = 0
for i in range(1, 11):
    case4_total = case4_total + i
print('case4-2', case4_total)

# case5
case5_total = 0
for i in range(1, 11):
    case5_total += i
print('case5', case5_total)

# case6
n = 10
print('case6', (n*(n+1))//2)

# case7
a = list(range(1, 11))
print('case7', sum(a))

# case8
print('case8', sum(range(1, 11)))

# case9
print('case9', 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10)

# case10(invalid)
print('case10', 55)

# case11(reduce)
# reduce 함수는 다음과 같이 iterable 의 요소들을 function 에 대입하여 결국 하나의 결과값을 리턴해 주는 함수이다
print('case11', reduce(lambda x, y: x + y, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))

# case12(reduce, for)
print('case12', reduce(lambda x, y: x + y, [x for x in range(1, 11)]))

# case13(reduce, list)
print('case13', reduce(lambda x, y: x + y, range(1, 11)))

