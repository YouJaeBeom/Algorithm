import numpy as np
print("Merge sort")

def mergesort(arr,start,end):
    print("start:", start, "mid",  int((start + end) / 2), "end:", end)
    print(arr[start:end])
    if(start<end-1):
        mid = int((start + end) / 2)
        leftarr=mergesort(arr, start, mid)
        rightarr=mergesort(arr, mid, end)
        return sort(leftarr,rightarr)

def sort(left,right):
    sortarr=[]
    i=0
    j=0
    print("left:",left,"right:",right)
    while(i<len(left)) & (j<len(right)):
        if left[i]<right[j]:
            sortarr.append(left[i])
            i+=1
        else:
            sortarr.append(right[j])
            j+=1

    ## 비교하고 sort하고 나서 혹시 남은 배열처리
    while i<len(left) :
        sortarr.append(left[i])
        i+=1
    while j<len(right):
        sortarr.append(right[j])
        j+=1
    print("\nsortarr :",sortarr,"\n")
    return sortarr



arr=[37,10,22,30,35,13,25,24]
start=0
end=len(arr)
result=mergesort(arr,start,end)
print("result : ",result)