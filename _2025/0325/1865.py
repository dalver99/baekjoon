import sys, heapq
input = sys.stdin.readline
INF = int(1e9)
TC = int(input())
for _ in range (TC):
    n,m,w = map(int,input().split())
    graph = [[] for _ in range (n+1)]
    for _ in range (m):
        start,end,weight = map(int,input().split())
        graph[start].append((weight,end))
    for _ in range (w):
        start,end,weight = map(int,input().split())
        graph[start].append((-weight,end))

    

    #print(graph)

def dijkstra(X):
    print()

#아 안풀어요 무슨 밸만포드였어
