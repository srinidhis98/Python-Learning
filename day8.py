'''
average number of hours worked per nurse on this day
'''


def avgwork(a, b, c, d, e, f, nurses):
    totalhrs = float(a+b+c+d+e+f)
    temp = float(totalhrs+ nurses)
    avghrs = totalhrs/nurses
    return avghrs


howard = 8
pease = 10
campbell = 9
grace = 8
mccarthy = 7
murphy = 12
nurses = 6
print(avgwork(howard, pease, campbell, grace, mccarthy, murphy, nurses))
