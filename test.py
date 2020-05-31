from numpy import sort


# def fun():
#     students = int(input())
#     mark_list = {}
#     for i in range(students*2):
#         print(i)
#         name = input()
#         mark = int(input())
#         mark_list[name] = mark
#
#     min = []
#     for key, value in mark_list.items():
#         min.append(value)
#         # print(min)
#
#     min.sort()
#     print(min)
#
#
# fun()


# def fun():
#     students = int(input())
#     mark_list = {}
#     # mark_set = set()
#     for i in range(students):
#         name = input()
#         mark = int(input())
#         mark_list[name] = mark
#
#     print(set(list(mark_list.values())))
# def fun():
#     students = int(input())
#     mark_list = []
#     for i in range(students):
#         name = input()
#         mark = int(input())
#         mark_list.append([name, mark])
#
#     mark_list[][1].sort()
#     print(mark_list)
#
#
#
#
#
# fun()
#
# l1 = [1,2,3,4]
# print(l1
#
# [l1[0]+1])


testcase = int(input())

for i in range(testcase):
    dishes = []
    item = int(input())
    for i in range(item):
        typeof_item = int(input())
        dishes.append(typeof_item)
    length = len(dishes)
    ele = 1
    cnt = [0]
    for j in range(length):
        if ele == dishes[j]:
            cnt.insert(ele, ele)
            if ele == dishes[j + 1]:
                continue
            elif ele == dishes[j + 2] and j < length:
                cnt.insert(ele, ele+1)

    sort(cnt)
    print(cnt.index() + 1)


