from random import randrange

def selectionsort(arr,findindex):
    if len(arr) <= 1:
        print("end",arr)
        return arr
    index=randrange(0, len(arr) )
    pivot = arr[index]

    lesser_arr, equal_arr, greater_arr = [], [], []
    for num in arr:
        if num < pivot:
            lesser_arr.append(num)
        elif num > pivot:
            greater_arr.append(num)
        else:
            equal_arr.append(num)
    arr= lesser_arr + equal_arr + greater_arr

    pivotindex=len(lesser_arr)
    print("left : ", arr[:pivotindex],"right : ", arr[pivotindex:])

    if findindex<=pivotindex :
        #내가 찾고자하는 몇번째 큰수가 왼쪽에 있다.
        arr=arr[:pivotindex]
        findindex=findindex
        print("@@@@@@@@@@@@@@@@@@@@@@@@@@왼쪽으로 찾아간다.")
        print("arr:", arr, "find", findindex)
        selectionsort(arr, findindex)
    else:
        # 내가 찾고자하는 몇번쨰 큰수가 오른쪽에 있다.
        arr=arr[pivotindex:]
        findindex-=pivotindex

        print("arr:", arr, "find", findindex)
        selectionsort(arr, findindex)




arr=[6,3,11,9,12,2,8,15,18,10,7,14]
findindex=int(input("몇번째 숫자:"))
selectionsort(arr,findindex)

