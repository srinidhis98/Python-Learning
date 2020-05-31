'''
Calculation part of the total cost of gifts
3 sweaters bought each at 68
computer game bought each at 75
bracelet bought each at 43
returned 1 bracelet with full refund and extra 10 rupees discount on computer_game
'''

gifts = {'sweater': [3, 68], 'computer_game': [1,75], 'bracelet': [2, 43]}
total = 0
for value in gifts.values():
    total += value[0] * value[1]
total = total - gifts['bracelet'][1] - 10
print(total)