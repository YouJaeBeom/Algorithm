import operator


def mst(L):
    # 가중치기준으로 오름차순정렬
    L=sorted(L.items(), key=operator.itemgetter(1))
    print("가중치 오름차순된 선분",L)

    # point갯수 파악
    point=[]
    for path in [L[i][0] for i in range(0,len(L))]:
        path.split("-")
        point.append(path[0])
        point.append(path[2])
    point = list(set(point))
    point_count=len(point) # point 갯수
    print("point", point)
    print("point_count ", point_count - 1)

    # 한 점과 연결된 점들 찾기
    link_point=[]
    for i in range(0,point_count):
        link_point.append([])
        for path in [L[i][0] for i in range(0,len(L))]:
            path.split("-")
            if (point[i]==path[0]):
                link_point[i].append(path[2])
            elif (point[i]==path[2]):
                link_point[i].append(path[0])
    print("link_point",link_point)


    T = []
    i=0
    makecycle(T, link_point, point)
    while (len(T) < point_count - 1):
        # L[i]를 T에 넣는다.
        T.append(L[i])
        i=i+1
        makecycle(T, link_point, point)
        # T list를 확인해서 사이클이 만들어지는지 확인한다.
        """if (makecycle(T,link_point,point)):
            T.pop(L[i])"""
        # 사이클이 만들어진다면 pop한다.
        # 그렇지 않는다면 계속 point갯수-1 한 만큼 돌도록 한다.

    print(T)
    return T

def makecycle(T,link_point,point):
    if(len(T)>1):
        for path in [T[i][0] for i in range(2, len(T))]:
            path.split("-")
            s1_index=point.index(path[0])
            s2_index=point.index(path[2])
            #link_point[s1_index].index(path[0])
            #link_point[s2_index].index(path[2])
            print(path[0],"//",path[2])
            while(link_point[s1_index].index(path[0])):

            print(link_point[s1_index].index(path[0]),"//",link_point[s2_index].index(path[2]))
            #
    else:
        print("아직")
    return

L={"a-e":4,"a-b":8,"a-d":2,"b-d":4,"b-f":2,"b-c":1,"d-f":7,"d-e":3,"e-f":9,"c-f":1}
print("가중치 오름차순되기 전 선분",L)
T=mst(L)
print("kruskalMST :",T)