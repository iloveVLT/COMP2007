# cgoh2475
# Assignment 2 Q2(b) iv. D+C
n=int(input()) # read in how many points
final=[] #[((float)x1,(float)x2,(int)imp)] 
points=[] #[((float)x1,(float)x2,(int)imp)] 

for i in range(n):# read in P
    temp_id="p"+str(i+1) #point id "pi" 0<i<l+1
    temp=input()
    temp_x1=float((temp.split(' '))[0]) # x1
    temp_x2=float((temp.split(' '))[1]) # x2
    temp_imp=0 # importance initially 0 for all

    points.append((temp_x1,temp_x2,temp_imp))

def merge(p1,p2):
    i=0
    j=0
    c=0 # status
    # sort p and q by x2
    px2_sort=sorted(p1, key=lambda e: e[1])
    qx2_sort=sorted(p2, key=lambda e: e[1])
    m_points=[]
    l=len(p1)
    r=len(p2)

    m_points.extend(px2_sort)
    while j<r:
    # (x1,x2,imp)
        tempq=qx2_sort[j] 
        qx1=tempq[0]
        qx2=tempq[1]
        q_imp=tempq[2]
        if i!=l and j!=r: # while still have P to go through
            tempp=px2_sort[i] 
            px1=tempp[0]
            px2=tempp[1]
            p_imp=tempp[2]

            if px1==qx1 or qx2 <= px2:
                m_points.append((qx1,qx2,q_imp+c))
                j+=1
            else:
                c+=1
                i+=1
        else: # done sweeping all P's
            m_points.append((qx1,qx2,q_imp+c))
            j+=1
    return m_points


def divideAndConquer(p):
    if len(p) == 0 or len(p)==1:
        return p
    middle=round(len(p)/2)
    a=divideAndConquer(p[:middle])
    b=divideAndConquer(p[middle:])
    return merge(a,b)

# sort by x1
points=sorted(points, key=lambda e: e[0])
final=divideAndConquer(points)
final=sorted(final,key=lambda e: (e[0],e[1]))
for f in range(len(final)):
    print((final[f])[2])

