def mergeSort(list):
    if len(list) == 1:
        return list

    left, right = split(list)
    left = mergeSort(left)
    right = mergeSort(right)
    return merge(left, right)

def merge(left, right):
    sorted = []
    while left and right:
        if left[0] < right[0]:
            sorted.append(left[0])
            left.pop(0)
        else:
            sorted.append(right[0])
            right.pop(0)
    while left:
        sorted.append(left[0])
        left.pop(0)
    while right:
        sorted.append(right[0])
        right.pop(0)
    return sorted

def split(list):
    middle = len(list)//2
    left = list[:middle]
    right = list[middle:]
    return left, right

def isSorted(list):
    if len(list) == 0 or len(list) == 1:
        return True
    return list[0] < list[1] and isSorted(list[1:])
