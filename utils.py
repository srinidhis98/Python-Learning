def find_max(numbers):
    maxim =  numbers[0]
    for num in numbers:
        if (num > maxim):
            maxim = num

    return maxim