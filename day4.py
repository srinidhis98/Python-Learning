hotdogs = 400
packets = 8
multiplicand = 1
intermediate = 0
while True:
    intermediate = packets * multiplicand
    if intermediate == hotdogs:
        print(multiplicand)
        break

    else:
        multiplicand += 1

'''
Jack bought 400 hotdogs for the school picnic if they were contained in packages of 8 hotdogs. how many total packages did he buy?
python program without / or % operator
'''
