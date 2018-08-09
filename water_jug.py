from __future__ import absolute_import
from __future__ import division
from __future__ import print_function


def gcd(a,b):
    if b==0:
        return a
    else:
        return gcd(b,a%b)
    
m=int(input("value of m : "))
n=int(input("value of n : "))

listk=[]
listk.append(0)

cp=0
cm=0

listcpcm = [0,0]
liststeps = [0,0]
#int k=0


val = gcd(m,n)
d=int(input("value of d : "))
k=0
valdd=d/val
dec, point = divmod(valdd, 1)
if point!=0:
    print("Problem is unsolvable as the value is %d"%valdd)
else:
    print("Problem is solvable as the value is %d"%valdd)

print("k is  %d"%0)

def kislessd(k,d,listcpcm):
    if (k!=d and k<n):
        k=k+m
        listk.append(k)
        listcpcm[0]=listcpcm[0]+1
        print("k is  %d: "%k)
        if (k==d or k>n):
            kisgreatn(k,n,listcpcm)
        if(k!=d and k<n):
            kislessd(k,d,listcpcm)
                     
def kisgreatn(k,n,listcpcm):
    if k>n:
        k=k-n
        listk.append(k)
        listcpcm[1]=listcpcm[1]+1
        print("k is  %d: "%k)        
    if(k>n):
        kisgreatn(k,n,listcpcm)
    if(k<d or k<n):
        kislessd(k,d,listcpcm)
   
        
kislessd(k,d,listcpcm)

print("value of number of additions    = %d" %listcpcm[0])
print("value of number of subtractions = %d" %listcpcm[1])
