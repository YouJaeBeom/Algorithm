import operator


def mst(L):
    L=sorted(L.items(), key=operator.itemgetter(1))
    print("가중치 오름차순된 선분",L)

    # point갯수 파악
    point=[]
    for path in [L[i][0] for i in range(0,len(L))]:
        path.split("-")
        point.append(path[0])
        point.append(path[2])
    point = set(point)
    point_count=len(point) # point 갯수


    T = []
    i=0
    print("point", point)
    print("point_count ",point_count - 1)
    while (len(T) < point_count - 1):
        T.append(L[i])
        i = i + 1

    print(T)
    return T







L={"a-e":4,"a-b":8,"a-d":2,"b-d":4,"b-f":2,"b-c":1,"d-f":7,"d-e":3,"e-f":9,"c-f":1}
print("가중치 오름차순되기 전 선분",L)
T=mst(L)
print("kruskalMST :",T)