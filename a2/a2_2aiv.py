# cgoh2475
# Assignment 2 Q2(a) iv. Merge
n=int(input()) # read in how many points
final=[] #[((float)x1,(float)x2,(int)imp)] 

# list of tuples sorted by x2 [(x1,x2,imp)]
px2_sort=[] 
qx2_sort=[]

l=int(input())
for i in range(l):# read in P
    temp_id="p"+str(i+1) #point id "pi" 0<i<l+1
    temp=input()
    temp_x1=float((temp.split(' '))[0]) # x1
    temp_x2=float((temp.split(' '))[1]) # x2
    temp_imp=int((temp.split(' '))[2]) # importance

    # put P in final
    final.append((temp_x1,temp_x2,temp_imp))

    px2_sort.append((temp_x1,temp_x2,temp_imp))

r=int(input())
for i in range(r):# read in Q
    temp_id="q"+str(i+1) #point id "pi" 0<i<r+1
    temp=input()
    temp_x1=float((temp.split(' '))[0]) # x1
    temp_x2=float((temp.split(' '))[1]) # x2
    temp_imp=int((temp.split(' '))[2]) # importance
    qx2_sort.append((temp_x1,temp_x2,temp_imp))

# sort p and q by x2 (for this question already sorted by x2: uncomment if not sorted)
#px2_sort=sorted(px2_sort, key=lambda e: e[1])
#qx2_sort=sorted(qx2_sort, key=lambda e: e[1])

k=r
i=0
j=0
c=0 # counter
# sweep p vertically and compare x2 (all x1 from Q is guaranteed bigger than P)
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
            final.append((qx1,qx2,q_imp+c))
            j+=1
        else:
            c+=1
            i+=1
    else: # done sweeping all P's
        final.append((qx1,qx2,q_imp+c))
        j+=1

# sort by x1,x2
final=sorted(final,key=lambda e: (e[0],e[1]))
for f in range(n):
    print((final[f])[2])
