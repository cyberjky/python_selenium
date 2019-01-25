# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
# user_input = int(input())
user_input = int(input())

for i in range(1, user_input+1):
    if i == user_input:
        print(i)
    elif user_input % i == 0:
        print(i, end=" ")