from random import randrange

def prim(L):
    T=[]
    point,point_count=getpoint(L)
    #p=point[randrange(0, point_count - 1)]
    p=point[2]
    print("p:",p)

    # weight list,visited list
    point_weight=[]
    point_visited = []
    for i in range(0,point_count):
        point_weight.append(100000)
        point_visited.append("false")
    point_weight[point.index(p)]=0
    point_visited[point.index(p)] = "true"
    print(point)
    print(point_weight)
    print(point_visited)

    index = 0
    lines = []
    for list in L:
        u, v, weight = list
        if u == p or v == p:
            lines.append(index)
        index = index + 1
    print(lines)
    # 임의의 점에서 제일 가까운선분 가져오기
    line_weight = []
    for line in lines:
        u, v, weight = L[line]
        line_weight.append(weight)

    u,v,weight=L[lines[line_weight.index(min(line_weight))]]
    if u == p:
        point_weight[point.index(v)] = min(line_weight)
        point_visited[point.index(v)] = "true"
    elif v == p:
        point_weight[point.index(u)] = min(line_weight)
        point_visited[point.index(u)] = "true"
    print(point)
    print(point_weight)
    print(point_visited)
    T.append(L[lines[line_weight.index(min(line_weight))]])

    #시작
    while(len(T)<point_count):
        u, v
    return T

def getpoint(L):
    # point갯수 파악
    point = []
    u1 = ""
    for list in L:
        u, v, weight = list
        if u1 != u:
            u1 = u
            point.append(u)
    for list in L:
        u, v, weight = list
        if v not in point:
            point.append(v)
    point_count = len(point)  # point 갯수
    print("point", point)
    return  point,point_count

L=[("a","e",4),("a","b",3),("a","d",2),("b","d",4),("b","f",2),("b","c",1),("c","f",1),("d","f",7),("d","e",5),("e","f",9)]
print("가중치 오름차순되기 전 선분",L)

T=prim(L)

print("primMST :",T)