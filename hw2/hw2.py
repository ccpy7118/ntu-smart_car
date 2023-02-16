import cv2 
import numpy as np 
import matplotlib.pyplot as plt
import pandas as pd
from PIL import Image
from skimage import measure
import math
import random

count=0
tmax=100000
tnow=tmax
tmin=1
r=0.95
message=17
tao=0.001
vnow=208.55999994277954
vbest=vnow
vbestforever=vnow
C=np.array([0.52,0.6,0.52,0.6,0.52,0.6,0.92,0.52,0.6,0.68,0.52,0.76,0.52,0.52,0.68,0.52,0.52])
T=np.array([50,5,5,5,5,5,10,10,10,10,50,100,100,100,1000,1000,1000])
P=np.array([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16])
B=np.zeros([message])
Q=np.zeros([message])
R=np.zeros([message])
newP=np.zeros([message])

def change(C,T,P,m,n):#找鄰居的解，用兩值互換的方法
    tmp=C[m]
    C[m]=C[n]
    C[n]=tmp
    tmp=T[m]
    T[m]=T[n]
    T[n]=tmp
    tmp=P[m]
    P[m]=P[n]
    P[n]=tmp
    return 0

def summary(R):
    add=0
    for k in range(message):
        add=add+(R[k])
    return add

def objective(C,T,P,tmax,tmin,r,message,tao):#算此順序下的總和
    k=0
    for k in range(message):
        B[k]=C[k]
    i=0
    k=0   
    for k in range(message):
        for i in range(k,message,1):
            if C[i]>B[k]:  
                B[k]=C[i]
    k=0
    j=0
    flag=1
    tmp=np.zeros([message])
    rhs=np.zeros([message])
    for k in range(message):
        flag=1
        Q[k]=B[k]
        while flag==1:
            j=0
            tmp[k]=0
            for j in range(k):
                tmp[k]=tmp[k]+math.ceil((Q[k]+tao)/T[j])*C[j]
            rhs[k]=B[k]+tmp[k]
            if rhs[k]+C[k]>T[k]:
                R[k]=1500
                break
            elif rhs[k]+C[k]<=T[k]:
                if Q[k]==rhs[k]:
                    R[k]=Q[k]+C[k]
                    flag=0    
                elif Q[k]!=rhs[k]:
                    Q[k]=rhs[k]
    u=summary(R)                
    return u               

print(objective(C,T,P,tmax,tmin,r,message,tao))  #印初始的總和208.56

evetime_value = []
num=0
while True:
    if tnow<=tmin:
        break
    for i in range(15):
        num+=1
        m=random.randint(0, 8)
        n=random.randint(9, 16)
        change(C,T,P,m,n)
        vnow=objective(C,T,P,tmax,tmin,r,message,tao)
        diff=vnow-vbest
        if(vnow<vbestforever):#將出現過最小的總和值存入vbestforever
            vbestforever=vnow
        if diff<=0:
            #count=count+1  
            #print(objective(C,T,P,tmax,tmin,r,message,tao),count) 
            vbest=vnow
            print(objective(C,T,P,tmax,tmin,r,message,tao),1) 
            evetime_value.append(vnow)
        elif diff>0:
            prob =math.exp(-diff/tnow)
            randum=random.uniform(0,1)
            if randum<prob:
                vbest=vnow
                print(objective(C,T,P,tmax,tmin,r,message,tao),2)
                evetime_value.append(vnow)
            elif randum>=prob:
                change(C,T,P,m,n)
                vnow=objective(C,T,P,tmax,tmin,r,message,tao)   
    tnow=tnow*r
print(objective(C,T,P,tmax,tmin,r,message,tao),3)   
for i in range(17):
    print("message",i,"的priority為:",P[i])
print("最佳的summation of the worst-case response time:",vbestforever) 
print(num)
plt.figure(figsize = (10,6))
plt.xlabel("Iteration",fontsize = 15)
plt.ylabel("value",fontsize = 15)
plt.plot(evetime_value,linewidth = 1, label = "smallest value ever", color = 'r')
plt.legend()
plt.show()    
    
    
for i in range(17):
    newP[P[i]]=i
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    