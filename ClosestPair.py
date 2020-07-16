from math import sqrt


def find_d(arr):
    d=[]
    for i in range(0,len(arr)):
        for l in range(i+1,len(arr)):
            d.append( ((sqrt((arr[i][0] - arr[l][0])**2 + (arr[i][1] - arr[l][1])**2) ), arr[i],arr[l]))
    d=min(d)
    return d

def closestpair(arr):
    if len(arr)<=3:
        return find_d(arr)
    midindex=int(len(arr)/2)
    print(arr[:midindex], "//", arr[midindex:])
    leftpair = closestpair(arr[:midindex])
    rightpair = closestpair(arr[midindex:])
    minpair=min(leftpair,rightpair)
    return minpair

def midclosestpair(pair,arr):
    midindex = int(len(arr) / 2)
    d = int(pair[0])
    print("arr",arr[midindex])
    dl=arr[midindex][0]-d
    dr=arr[midindex][0]+d
    print(dl,dr)
    for i in range(0,len(arr)):
        if (arr[i][0]>=dl):
            startindex=i
            break
    print("startindex", startindex)

    for l in range(len(arr)-1,0,-1):
        if (arr[l][0]<=dr):
            endindex=l
            break
    print("endindex",endindex)
    midpair = find_d(arr[startindex:endindex])
    result=min(pair,midpair)
    print("pair", pair)
    print("midpair", midpair)
    return result




arr=[ [1,7],[1,9],[2,3],[2,4],[3,4],[3,7],[4,2],[4,8],  [5,1],[5,5],[6,7],[6,1],[7,3],[7,7],[8,4],[8,9] ]
pair=closestpair(arr)
print("pair",pair)
result=midclosestpair(pair,arr)

print("result",result)
#print("minpair",minpair)

#print("result:",arr1)


