

'''
Doubled sided stair case pattern
5
             *  *
             *  *
          *  *  *  *
          *  *  *  *
       *  *  *  *  *  *
       *  *  *  *  *  *
    *  *  *  *  *  *  *  *
    *  *  *  *  *  *  *  *
 *  *  *  *  *  *  *  *  *  *
 *  *  *  *  *  *  *  *  *  *

'''




num = int(input())

for i in range(1, num+1):
    print('   '*(num - i) + ' * ' * (i * 2))
    print('   '*(num - i) + ' * ' * (i * 2))