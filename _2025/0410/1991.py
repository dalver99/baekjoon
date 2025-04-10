import sys
input = sys.stdin.readline

N = int(input())
tree = {}
#ord A = 65
for i in range (N):
    now,left,right = map(str,input().split())
    tree[now] = (left,right) #점은 46-65 = -19이 들어간다
#print(tree)
jeon = []
def dfs_a(V): #방문 즉시 visited, print
    # print(V)
    jeon.append(V)
    left,right = tree[V]
    if left != ".":
        dfs_a(left)
    if right != ".":
        dfs_a(right)


dfs_a("A")
print("".join(jeon))

joong = []
def dfs_c(V): #최종점일때만 print.
    # print(V)
    left,right = tree[V]
    if left != ".":
        dfs_c(left)
        joong.append(V)
    else:
        joong.append(V)
    if right != ".":
        dfs_c(right)


dfs_c("A")
print("".join(joong))


who = []
def dfs_b(V): #최종점일때만 print.
    # print(V)
    left,right = tree[V]
    if left != ".":
        dfs_b(left)
    if right != ".":
        dfs_b(right)
        who.append(V)
    else:
        who.append(V)


dfs_b("A")
print("".join(who))


# def dfs_b(V): 
