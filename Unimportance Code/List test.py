
list1 = [2,4,6,2,3,8,1,4,9,2,7,6,3,5,8,6,8,7,3,1,5,6]
if list1:
    list1.sort()
    last = list1[-1]
    for i in range(len(list1)-2,-1,-1):
        if last == list1[i]: del list1[i]
        else: last = list1[i]
print(list1)
