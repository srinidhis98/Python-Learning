def bubble_sort(array):
    n = len(array)
    for i in range(n):
        for j in range(i, n):
            if array[i] > array[j]:
                temp = array[i]
                array[i] = array[j]
                array[j] = temp

    return array


arr = [5, 6, 1, 0, 9, 7, 88]
print(bubble_sort(arr))


'''
Bubble sort
'''