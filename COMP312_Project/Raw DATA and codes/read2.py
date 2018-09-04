import datetime, time
# -*- coding: utf-8 -*-
ES= []
inter_arr=[]
all_arrival=[]
W=0
w_list=[]

import numpy as np
WS=[]
WQ=[]

with open("minping", 'r') as f:
    d= f.readline()
    a, num=d.split("#")
    Num_observation= int(num)

cu=[]
for i in range (1,Num_observation+1):
    li=[]
    a=str(i)
    with open("minping", 'r') as fp:
        d1= fp.readline()
        d2= fp.readline()
        for line in fp:
            if "begin" in line or "end" in line:
                continue
            if(' '+a+'_') in line:
                time, tag= line.split("  ")
                li.append(float(time))
        cu.append(li)

#finish reading-> raw data representation
#Arrival records
for n in range(Num_observation):
    arr= cu[n][0]
    all_arrival.append(arr)
        
#Service time
for n in range(0, Num_observation):
    service_time=cu[n][2]- cu[n][1]
    ES.append(service_time)

#W
for n in range(0, Num_observation):
    W_time=cu[n][2]- cu[n][0]
    W+=W_time
    w_list.append(W_time)

#WS =completion-begin of service
for n in range(0, Num_observation):
    WS_time=cu[n][2]- cu[n][1]
    WS.append(WS_time)
    
#WQ =begin of service-arrival time
for n in range(0, Num_observation):
    WQ_time=cu[n][1]- cu[n][0]
    WQ.append(WQ_time)



with open("Hao", 'r') as f:
    d= f.readline()
    a, num=d.split("#")
    Num_observation= int(num)

cu=[]
for i in range (1,Num_observation+1):
    li=[]
    a=str(i)
    with open("Hao", 'r') as fp:
        d1= fp.readline()
        d2= fp.readline()
        for line in fp:
            if "begin" in line or "end" in line:
                continue
            if(' '+a+'_') in line:
                time, tag= line.split("  ")
                li.append(float(time))
        cu.append(li)
#finish reading-> raw data representation

#Arrival records
for n in range(Num_observation):
    arr= cu[n][0]
    all_arrival.append(arr)
#Service time
for n in range(0, Num_observation):
    service_time=cu[n][2]- cu[n][1]
    ES.append(service_time)

#W
for n in range(0, Num_observation):
    W_time=cu[n][2]- cu[n][0]
    W+=W_time
    w_list.append(W_time)

#WS =completion-begin of service
for n in range(0, Num_observation):
    WS_time=cu[n][2]- cu[n][1]
    WS.append(WS_time)
    
#WQ =begin of service-arrival time
for n in range(0, Num_observation):
    WQ_time=cu[n][1]- cu[n][0]
    WQ.append(WQ_time)
    

with open("Mark", 'r') as f:
    d= f.readline()
    a, num=d.split("#")
    Num_observation= int(num)

cu=[]
for i in range (1,Num_observation+1):
    li=[]
    a=str(i)
    with open("Mark", 'r') as fp:
        d1= fp.readline()
        d2= fp.readline()
        for line in fp:
            if "begin" in line or "end" in line:
                continue
            if(' '+a+'_') in line:
                time, tag= line.split("  ")
                li.append(float(time))
        cu.append(li)

#finish reading-> raw data representation
#Arrival records
for n in range(Num_observation):
    arr= cu[n][0]
    all_arrival.append(arr)

#Service time
for n in range(0, Num_observation):
    service_time=cu[n][2]- cu[n][1]
    ES.append(service_time)

#W
for n in range(0, Num_observation):
    W_time=cu[n][2]- cu[n][0]
    W+=W_time
    w_list.append(W_time)

#WS =completion-begin of service
for n in range(0, Num_observation):
    WS_time=cu[n][2]- cu[n][1]
    WS.append(WS_time)
    
#WQ =begin of service-arrival time
for n in range(0, Num_observation):
    WQ_time=cu[n][1]- cu[n][0]
    WQ.append(WQ_time)

#--------------#
for n in range(len(ES)):
    print "E(Service time): {0}".format(ES[n]/60.0)

for i in range(len(all_arrival)-1):
    d= (all_arrival[i+1]-all_arrival[i])
    if d>0:
        inter_arr.append(d/60.0)


for n in range(len(inter_arr)):
    print inter_arr[n]

print "#inter-arrival", len(inter_arr)
print "#ES", len(ES)


print "Waiting time in system for EACH CUSTOMER"
for i in range(len(w_list)):
    print i, w_list[i]/60.0, " min"

print W/(60.0)


print""
print "--WQ--"
print np.mean(WQ)/60.0

print""
print "--WS--"
print np.mean(WS)/60.0




