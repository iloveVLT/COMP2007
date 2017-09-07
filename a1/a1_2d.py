#cgoh2475
n=int(input()) #number of vertices
m=int(input())#number of edges

adjList={} # hashmap of key:(int)node, value: neighbours<(int)node,(float)weight>
for i in range(n):
    adjList[i]={}

pq={} #<string 'u,v',float w>
# add edges to adjacency list
for i in range(m):
    temp=input().split(' ') #u,v,weight
    neighbours_v1=adjList[int(temp[0])] #have to add both ways
    neighbours_v2=adjList[int(temp[1])]
    if int(temp[1]) not in neighbours_v1: #if edge not in graph add it
        neighbours_v1[int(temp[1])]=float(temp[2])
    if int(temp[0]) not in neighbours_v2:
        neighbours_v2[int(temp[0])]=float(temp[2])
        
    #add to pq ceebs
    edge_str=str(temp[0])+','+str(temp[1])
    #print(edge_str)
    pq[edge_str]=float(temp[2])
    
a=int(input()) #existing network
A=[[0 for x in range(2)] for y in range(a)]
for i in range(a):
    temp=input().split(' ') #u,v
    A[i]=[int(temp[0]),int(temp[1])]

# Graph Node
class Node:
        def __init__(self,num):
            self.data=num
            self.parent=num
            self.rank=0
            
# Disjoint Set - start
class DisjointSet:
    def __init__(self):
        self.hm={} #<int,node>
        
    def makeSet(self,v):
        self.hm[int(v)]=Node(v)

    def union(self,set1,set2):
        node1=self.hm[set1]
        node2=self.hm[set2]
        #print(type(node1),type(node1.parent))

        #print(node2.parent)
        parent1=self.hm[node1.parent]
        parent2=self.hm[node2.parent]
        
        #print(type(parent1),type(parent2))
        if parent1 is parent2: #same set
            return

        if parent1.rank>=parent2.rank:
            if parent1.rank==parent2.rank:
                parent1.rank+=1
            parent2.parent=parent1.data
        else:
            parent1.parent=parent2.data


    def findSet(self,node_id):
        u=self.hm[node_id]
        parent=self.hm[u.parent] #int parent id
        if parent is u:
            #print("return")
            return parent.data
        u.parent=self.findSet(u.parent) #path compression
       
        return u.parent

    def inSame(self,u,v):
        if self.findSet(u) is self.findSet(v):
            return True
        else:
            return False

# Disjoint Set - end
# algorithm start
#result MST init
T={}
for i in range(n):
    T[i]={}

# init union find
S=DisjointSet()
for k in adjList.keys():
    S.makeSet(k)

sum_mst=0
# add existing edges from A to tree AND union in set
for e in A:
    u=e[0]
    v=e[1]
    u_neighbours=adjList[u]
    v_neighbours=adjList[v]
    # find each other in neighbours
    uv_weight=float(u_neighbours[v])
    vu_weight=float(v_neighbours[u])
    if (uv_weight != vu_weight):
        print("m8 there's something wrong with ur gRAPH!")
        raise SystemExit
    elif  (uv_weight is None) or (vu_weight is None):
        print("can't find other node in neighbours...")
        raise SystemExit
    # weight + graph is very OK
    #add weight to sum
    sum_mst+=uv_weight
    # adding to result tree
    Tu_neighbours=T[u]
    Tv_neighbours=T[v]
    if int(v) not in Tu_neighbours:
        Tu_neighbours[int(v)]=float(uv_weight)
    if int(u) not in Tv_neighbours:
        Tv_neighbours[int(u)]=float(vu_weight) # why am i casting so much? just in case...??

    # union u,v in set S
    S.union(u,v)
    # delete after done so can get E\A
    del(u_neighbours[v])
    del(v_neighbours[u])
    # delete from PQ
    edge_str1=str(u)+','+str(v)
    edge_str2=str(v)+','+str(u)
    if edge_str1 in pq.keys():
        del(pq[edge_str1])
    elif edge_str2 in pq.keys():
        del(pq[edge_str2])
    
# sort in ascending order by value 
pq_sorted=sorted(zip(pq.values(),pq.keys())) # now array
#do kruskal
for e in pq_sorted: # pq_sorted[float weight,str 'u,v']
    edge=e[1].split(',')
    w=e[0]
    u=int(edge[0])
    v=int(edge[1])
    if S.inSame(u,v) is False:
        #add to T
        Tu_neighbours=T[u]
        Tv_neighbours=T[v]
        if int(v) not in Tu_neighbours:
            Tu_neighbours[int(v)]=float(w)
        if int(u) not in Tv_neighbours:
            Tv_neighbours[int(u)]=float(w)
        #union in S
        S.union(u,v)
        sum_mst+=float(w)

print(round(sum_mst,2))
