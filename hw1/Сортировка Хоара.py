from random import randint
def sort_h(a):
    if len(a) < 2:
        return a
    left = []
    right = []
    middle = []
    k = randint(0, len(a)-1)
    pivot = (a[0] + a[-1] + a[k])//3
    for i in range(len(a)):
        if a[i] > pivot:
            right.append(a[i])
        if a[i] == pivot:
            middle.append(a[i])
        if a[i] < pivot:
            left.append(a[i])
    sort_h(left)
    sort_h(right)
    a.clear()
    for i in left:
        a.append(i)
    for i in middle:
        a.append(i)
    for i in right:
        a.append(i)
    return a

