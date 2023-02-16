

# -*- coding: utf-8 -*-
"""
Created on Sun Sep 25 15:53:47 2022

@author: ccpy
"""

import cv2 
import numpy as np 
import matplotlib.pyplot as plt
import pandas as pd
from PIL import Image
from skimage import measure
import math

objective=0
message=17
tao=0.001

C=np.array([0.52,0.6,0.52,0.6,0.52,0.6,0.92,0.52,0.6,0.68,0.52,0.76,0.52,0.52,0.68,0.52,0.52])

T=np.array([50,5,5,5,5,5,10,10,10,10,50,100,100,100,1000,1000,1000])

B=np.zeros([message])

Q=np.zeros([message])

R=np.zeros([message],dtype='f4')

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
            #R[k]=300000
            break
        elif rhs[k]+C[k]<=T[k]:
            if Q[k]==rhs[k]:
                R[k]=Q[k]+C[k]
                flag=0
                
            elif Q[k]!=rhs[k]:
                Q[k]=rhs[k]
                
for k in range(message):
    objective=objective+R[k]
    #print(R[k])
print(objective)
    






























# -*- coding: utf-8 -*-
"""
Created on Sun Sep 25 15:53:47 2022

@author: ccpy
"""

import cv2 
import numpy as np 
import matplotlib.pyplot as plt
import pandas as pd
from PIL import Image
from skimage import measure
import math

objective=0
message=3
tao=0.1

C=np.array([10,30,20])

T=np.array([40,100,70])

B=np.zeros([message])

Q=np.zeros([message])

R=np.zeros([message],dtype='f4')

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
            R[k]=300000
            break
        elif rhs[k]+C[k]<=T[k]:
            if Q[k]==rhs[k]:
                R[k]=Q[k]+C[k]
                flag=0
                
            elif Q[k]!=rhs[k]:
                Q[k]=rhs[k]
                
for k in range(message):
    objective=objective+R[k]
    #print(R[k])
print(objective)
    
