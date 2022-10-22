from random import randrange

def prim(L):
    T=[]
    point,point_count=getpoint(L)
    #p=point[randrange(0, point_count - 1)]
    p=point[2]
    print("p:",p)

    ## 1번째
    #임의의 점과 연결된 선분 가져오기
    index=0
    lines=[]
    for list in L:
        u, v, weight = list
        if u == p or v == p:
            lines.append(index)
        index=index+1
    print(lines)
    # 임의의 점에서 제일 가까운선분 가져오기
    line_weight=[]
    for line in lines:
        u,v,weight=L[line]
        line_weight.append(weight)
    print("최소값",min(line_weight),"인덱스",line_weight.index(min(line_weight)))
    print("선분",L[lines[line_weight.index(min(line_weight))]],"선분의 인덱스",lines[line_weight.index(min(line_weight))])
    T.append(L[lines[line_weight.index(min(line_weight))]])


    ## 2번쨰
    u2,v2,weight=L[lines[line_weight.index(min(line_weight))]]
    L.pop(lines[line_weight.index(min(line_weight))])
    print(u2,v2)
    print("L", L)
    print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
    # 임의의 점과 연결된 선분 가져오기
    index = 0
    lines = []
    for list in L:
        u, v, weight = list
        if u == u2 or v == u2:
            lines.append(index)
        index = index + 1
    print(lines)

    index = 0
    lines1 = []
    for list in L:
        u, v, weight = list
        if u == v2 or v == v2:
            lines1.append(index)
        index = index + 1
    print(lines1)
    # 임의의 점에서 제일 가까운선분 가져오기
    line_weight = []
    for line in lines:
        u, v, weight = L[line]
        line_weight.append(weight)
    print("최소값", min(line_weight), "인덱스", line_weight.index(min(line_weight)))
    print("선분", L[lines[line_weight.index(min(line_weight))]], "선분의 인덱스", lines[line_weight.index(min(line_weight))])
    line_weight1 = []
    for line in lines1:
        u, v, weight = L[line]
        line_weight1.append(weight)
    print("@@@@@@@@@@@@@@@@@@@@@@@")
    print("최소값", min(line_weight1), "인덱스", line_weight1.index(min(line_weight1)))
    print("선분", L[lines1[line_weight1.index(min(line_weight1))]], "선분의 인덱스", lines1[line_weight1.index(min(line_weight1))])
    if min(line_weight) <= min(line_weight1):
        T.append(L[lines[line_weight.index(min(line_weight))]])
    elif min(line_weight) > min(line_weight1):
        T.append(L[lines1[line_weight1.index(min(line_weight1))]])

    #while(len(T)<point_count): ## 반환할 리스트의 개수가 점의 갯수보다 작을때까지

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