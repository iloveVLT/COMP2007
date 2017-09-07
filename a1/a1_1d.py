# cgoh2475
data=[]
    
n=int(input()) #number of vertices
m=int(input())#number of edges

adjList={} # hashmap of key:(int)node, value: neighbours<(int)node,(float)weight>
for i in range(n):
    adjList[i]={}

# add edges to adjacency list
for i in range(m):
    temp=input().split(' ')
    neighbours_v1=adjList[int(temp[0])] #have to add both ways
    neighbours_v2=adjList[int(temp[1])]
    if int(temp[1]) not in neighbours_v1: #if edge not in graph add it
        neighbours_v1[int(temp[1])]=float(temp[2])
    if int(temp[0]) not in neighbours_v2:
        neighbours_v2[int(temp[0])]=float(temp[2])
           
q=int(input())
#q=int(data[m+2]) # |Q|
Q=[[0 for x in range(2)] for y in range(q)]
for i in range(q):
    temp=input().split(' ')
    Q[i]=[int(temp[0]),temp[1]]

def dfs_path(start,end,visited=None):
    if visited is None:
        visited=[]
    if start in visited:
        return
    visited.append(start)

    if start not in adjList:
        print("Node %d not in graph!"%start)
        return
    neighbours=adjList[start]
    if end in neighbours:
        return True
    else:
        for v in neighbours:
            y=dfs_path(int(v),int(end),visited)
            if y is True:
                return True
    return False

for query in Q:
    result=dfs_path(int(query[0]),int(query[1]))
    if result is True:
        print('1')
    else:
        print('0')


