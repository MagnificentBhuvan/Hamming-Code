def findingr(exponent,data1,total):
    exponent=1<<exponent
    temp=5
    #print (exponent)
    for i in range(exponent+1,total+1):
        if exponent & i==exponent and i!=exponent :
            print (i)
            if temp==5:
                temp=int(data1[i-1])
            else:
                temp=temp^int(data1[i-1])
        #print (temp)
    return temp
        
data=bin(int(input("Enter the data")))
data=data[2:]
print (data)
noofbits=len(data)
length=noofbits-1
r=1
representation=[]
ii=1
rr=[]
while (pow(2,r)<(noofbits+r+1)):
    r=r+1
print (r)
for i in range(1,noofbits+r+1):
    if i in [pow(2,x) for x in range(noofbits)]:
        representation.append('r'+str(ii))
        #res=findingr(ii,data,noofbits+r)
        ii=ii+1
    else:
        representation.append(data[length])
        length=length-1
#representation.reverse()
print (representation)
#for j in range(r):
#    result=findingr(j)
for i in range(r):
   rr.append(findingr(i,representation,noofbits+r))
   print ("----------------")
for k in range(r):
    representation[representation.index('r'+str(k+1))]=rr[k]
print (representation)    
