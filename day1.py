'''
there was a teacher in a small town who loves coding and he wants to create a program which prints out the whole multipli
cation table of an entered number
Write a program for this problem.
'''



num = int(input("Enter a number"))

for i in range(1,11):
    print(f'{i} * {num} = {i*num}');