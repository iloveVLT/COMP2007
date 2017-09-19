c=0
impc=0
v=None
points={}
xcoord=[]
result=[]

# read in n
n=int(input())
for i in range(n): # read in x1
    temp=int(input())
    xcoord.append(temp)

# sort x1 in increasing order
xcoord.sort()

# sweep xcoord
for x in xcoord:
    tempx=x
    if tempx != v: # not same as prev x1
        v=int(tempx)
        if c!=1:
            impc+=c
        else:
            impc+=1
        c=1
    else: # same as prev x1
        c+=1
    result.append(impc)
    print(impc)
