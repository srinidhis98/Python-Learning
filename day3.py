def func(val):
    x = 500
    y = 0
    while True:
        x = x - (300 - y)
        if x == val:
            return True
        else:
            if x+y <= 300:
                y += x
                x = 500
                continue



val = int(input("Enter no of litres needed"))
x = 500
if val <= x:
    print(func(val))
elif val > x:
   res = func(val-x)
   # if res is None:
   #     print("Cant happen")
   # else:
   print(res)


'''
A chef was cooking something special which required exact 200 ml
water but he doesnt have 200 ml cup he has a 500 ml and a 300 ml cup 
but that dish required exactly 200 ml water


'''