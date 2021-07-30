#!/usr/bin/python3
while True:
    value = input("Integer, please [q to quit]: ")
    if value == 'q':      #выход
        break
    number = int(value)
    if number % 2 == 0:  #нечетное число
        continue
    print(number, "squared is", number * number)
