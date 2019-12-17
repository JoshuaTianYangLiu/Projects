from math import *

def area(a,b,c):
    sp=(a+b+c)/2
    # print (sp)
    return sqrt(sp*(sp-a)*(sp-b)*(sp-c))
def isValid(a,b,c):
    return a+b>c and b+c>a and a+c>b
p=18
cnt=0
for i in range(1,p-1):
    for j in range(i,p-i):
        k=p-i-j
        if isValid(i,j,k) and k>=j:
            print (i,j,k)
            cnt+=1
print (cnt)