def multiply(a, b):
    if b == 0:
        return 0
    if b > 0:
        return a + multiply(a, b - 1)
    if b < 0:
        return -multiply(a, -b)


print(multiply(1200000, 365))


'''
Multiply 2 numbers without * / bitwise operator and loop
'''