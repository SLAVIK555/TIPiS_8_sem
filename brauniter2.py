import numpy as np
import random as rnd

source_matr = np.array([
                        (5, -2, 3),
                        (0, 5, 2)
                       ])
#print("source_matr :\n {0}".format(source_matr[0][0]))

msize = 3
nsize = 2
m = list(range(msize))
n = list(range(nsize))
#print ("n :\n {0}".format(n))
mr = rnd.randint(0, 2)
nr = rnd.randint(0, 1)
#print(mr)
#print(nr)

for i in range(msize):
    #print(i)
    m[i]=source_matr[nr][i]
    #print(m)

for j in range(nsize):
    #print(j)
    n[j]=source_matr[j][mr]
    #print(n)

#print ("n :\n {0}".format(n))
#print(m[i])

print("K|ik|m0|m1|m2|minm|y2|jk|n0|n1|maxn|y1|miny1|maxy2|deltak")#n2|n3|
print("---------------------------------------------------------------")

fi1=0
fi2=0
psi1=0
psi2=0
psi3=0

k=1
miny1=1000000
maxy2=-100
while(True):
    m0=m[0]
    m1=m[1]
    m2=m[2]
    n0=n[0]
    n1=n[1]

    #minm=min(m)
    #maxn=max(n)
    minm, ik = min((minm, ik) for (ik, minm) in enumerate(m))
    maxn, jk = max((maxn, jk) for (jk, maxn) in enumerate(n))

    if(ik==0):
        psi1=psi1+1
    elif(ik==1):
        psi2=psi2+1
    elif(ik==2):
        psi3=psi3+1

    if(jk==0):
        fi1=fi1+1
    elif(jk==1):
        fi2=fi2+1
    #print(maxn)
    #print(ik)
    #print(jk)
    y2=minm/k
    y1=maxn/k

    if y1<miny1:
        miny1=y1

    if y2>maxy2:
        maxy2=y2

    deltak=miny1-maxy2

    print("K:"+str(k)+"|ik:"+str(ik)+"|m0:"+str(m0)+"|m1:"+str(m1)+"|m2:"+str(m2)+"|minm:"+str(minm)+"|y2:"+str(y2)+"|jk:"+str(jk)+"|n0:"+str(n0)+"|n1:"+str(n1)+"|maxn:"+str(maxn)+"|y1:"+str(y1)+"|miny1:"+str(miny1)+"|maxy2:"+str(maxy2)+"|deltak:"+str(deltak))#+"|n2:"+str(n2)+"|n3:"+str(n3)
    print("-----------------------------------------------------------------------------------------------------------------------------")

    for i in range(msize):
        #print(i)
        m[i]=source_matr[jk][i]
        #print(m)

    for j in range(nsize):
        #print(j)
        n[j]=source_matr[j][ik]
        #print(n)

    k=k+1
    if k==50:
        break

    if deltak < 0.001:
        break

print(fi1)
print(fi2)
print(psi1)
print(psi2)
print(psi3/k)
    #print(m[0])
#k=0
#m1=source_matr[0][0]
#m2=source_matr[0][1]
#m3=source_matr[0][2]
#print("K|ik|m1|m2|m3|y2|jk|n1|n2|n3|n4|y1|min_m|max_n|miny1|maxy2|delk\n")
#while(True)