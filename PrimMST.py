from random import randrange

def prim(L):
    point,point_count=getpoint(L)
    #p=point[randrange(0, point_count - 1)]
    p=point[2]
    print("p:",p)
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
    print("선분",point[line_weight.index(min(line_weight))],"선분의 인덱스",lines[line_weight.index(min(line_weight))])
    pass

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