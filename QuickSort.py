from random import randrange

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[randrange(0, len(arr) - 1)]
    lesser_arr, equal_arr, greater_arr = [], [], []
    for num in arr:
        if num < pivot:
            lesser_arr.append(num)
        elif num > pivot:
            greater_arr.append(num)
        else:
            equal_arr.append(num)
    return quick_sort(lesser_arr) + equal_arr + quick_sort(greater_arr)





arr=[6,3,11,9,12,2,8,15,18,10,7,14]

result=quick_sort(arr)
print("arr",arr)
print(result)
