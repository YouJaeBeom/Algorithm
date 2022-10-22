import numpy as np
print("Merge sort")
def merge_sort(arr):
    if len(arr) < 2:
        return arr

    mid = len(arr) // 2
    low_arr = merge_sort(arr[:mid])
    high_arr = merge_sort(arr[mid:])

    merged_arr = []
    l = h = 0
    while l < len(low_arr) and h < len(high_arr):
        if low_arr[l] < high_arr[h]:
            merged_arr.append(low_arr[l])
            l += 1
        else:
            merged_arr.append(high_arr[h])
            h += 1
    merged_arr += low_arr[l:]
    merged_arr += high_arr[h:]
    return merged_arr

def mergesort(arr):
    def sort(start,end):
        print("start:", start, "mid",  int((start + end) / 2), "end:", end)
        print(arr[start:end])
        if end - start < 2:
            return
        mid = int((start + end) / 2)
        sort(start,mid)
        sort(mid,end)
        temp=merge(start,mid,end)
        return temp
    def merge(start,mid,end):
        temp = []
        l, h = start, mid

        while l < mid and h < end:
            if arr[l] < arr[h]:
                temp.append(arr[l])
                l += 1
            else:
                temp.append(arr[h])
                h += 1

        while l < mid:
            temp.append(arr[l])
            l += 1
        while h < end:
            temp.append(arr[h])
            h += 1

        for i in range(start, end):
            arr[i] = temp[i - start]
        print("tmp",temp)
        return temp
    return sort(0, len(arr))




arr=[37,10,22,30,35,13,25,24]
result=merge_sort(arr)
result1=mergesort(arr)

print("result : ",result)
print("result1 :",result1)