#Andy- data archiving
# -*- coding: utf-8 -*-
import datetime, time
import numpy as np
def dateDiffInSeconds(date1, date2):
    time_delta = date2 - date1
    return time_delta.days*24*3600 + time_delta.seconds
ES=[]
all_arrival=[]
sum_W=0
w_list=[]
Ws=[] #[Complete- Begin]
Wq=[] #[Begin- arrival]


filename= "April24.txt"
with open(filename,'r') as fp:
    d1= fp.readline()
    d2= fp.readline()
    d3= fp.readline()
    d4= fp.readline()
    d5= fp.readline()
    
    From, timeFrom= d3.split(" ")
    start= [int(i) for i in timeFrom.split(":")]
    To, timeTo= d4.split(" ")
    end= [int(i) for i in timeTo.split(":")]
    st= datetime.datetime(2017, 04,24, start[0], start[1], start[2])
    en= datetime.datetime(2017, 04,24, end[0], end[1], end[2])
    dif= dateDiffInSeconds(st, en)
   
    sum_s=0
    sum_w=0
    numOfArrival=0
    for line in fp:
        No_customer, Arrival, Begin, Completion= line.split(" ")
        arrival = [int(n) for n in Arrival.split(":")]
        begin =[int(n) for n in Begin.split(":")]
        complete =[int(n) for n in Completion.split(":")]

        #Ws
        Ws1= datetime.datetime(2017, 04, 24, begin[0],begin[1],begin[2])
        Ws2= datetime.datetime(2017, 04, 24, complete[0],complete[1],complete[2])
        Ws.append(dateDiffInSeconds(Ws1, Ws2)/60.0)

        #Wq
        WQ1= datetime.datetime(2017, 04, 24, arrival[0],arrival[1],arrival[2])
        WQ2= datetime.datetime(2017, 04, 24, begin[0],begin[1],begin[2])
        Wq.append(dateDiffInSeconds(WQ1, WQ2)/60.0)

        #waiting Time 
        t1= datetime.datetime(2017, 04, 24, arrival[0],arrival[1],arrival[2])
        t2= datetime.datetime(2017, 04, 24, begin[0],begin[1],begin[2])
        all_arrival.append(t1)
        
        #service time
        s1= datetime.datetime(2017, 04, 24, begin[0],begin[1],begin[2])
        s2= datetime.datetime(2017, 04, 24, complete[0],complete[1],complete[2])
        ES.append(dateDiffInSeconds(s1, s2)/60.0)
        
        #average service time
        a1= datetime.datetime(2017, 04, 24, begin[0],begin[1],begin[2])
        a2= datetime.datetime(2017, 04, 24, complete[0],complete[1],complete[2])
        sum_s+=dateDiffInSeconds(a1,a2)

        #average wait time
        w1= datetime.datetime(2017, 04, 24, arrival[0],arrival[1],arrival[2])
        w2= datetime.datetime(2017, 04, 24, begin[0],begin[1],begin[2])
        sum_w+=dateDiffInSeconds(w1,w2)
        numOfArrival+=1

        #W time spent in system
        W_1= datetime.datetime(2017, 04, 24, arrival[0],arrival[1],arrival[2])
        W_2= datetime.datetime(2017, 04, 24, complete[0],complete[1],complete[2])
        sum_W+=(dateDiffInSeconds(W_1,W_2)/60.0)
        w_list.append(dateDiffInSeconds(W_1,W_2)/60.0)




filename= "April24.txt"
with open(filename,'r') as fp:
    d1= fp.readline()
    d2= fp.readline()
    d3= fp.readline()
    d4= fp.readline()
    d5= fp.readline()
    
    From, timeFrom= d3.split(" ")
    start= [int(i) for i in timeFrom.split(":")]
    To, timeTo= d4.split(" ")
    end= [int(i) for i in timeTo.split(":")]
    st= datetime.datetime(2017, 04,24, start[0], start[1], start[2])
    en= datetime.datetime(2017, 04,24, end[0], end[1], end[2])
    dif= dateDiffInSeconds(st, en)
   
    sum_s=0
    sum_w=0
    numOfArrival=0
    for line in fp:
        No_customer, Arrival, Begin, Completion= line.split(" ")
        
        arrival = [int(n) for n in Arrival.split(":")]
        begin =[int(n) for n in Begin.split(":")]
        complete =[int(n) for n in Completion.split(":")]

        #Ws
        Ws1= datetime.datetime(2017, 04, 24, begin[0],begin[1],begin[2])
        Ws2= datetime.datetime(2017, 04, 24, complete[0],complete[1],complete[2])
        Ws.append(dateDiffInSeconds(Ws1, Ws2)/60.0)

        #Wq
        WQ1= datetime.datetime(2017, 04, 24, arrival[0],arrival[1],arrival[2])
        WQ2= datetime.datetime(2017, 04, 24, begin[0],begin[1],begin[2])
        Wq.append(dateDiffInSeconds(WQ1, WQ2)/60.0)

        #waiting Time
        t1= datetime.datetime(2017, 04, 24, arrival[0],arrival[1],arrival[2])
        t2= datetime.datetime(2017, 04, 24, begin[0],begin[1],begin[2])
        all_arrival.append(t1)
        
        #service time
        s1= datetime.datetime(2017, 04, 24, begin[0],begin[1],begin[2])
        s2= datetime.datetime(2017, 04, 24, complete[0],complete[1],complete[2])
        ES.append(dateDiffInSeconds(s1, s2)/60.0)
        
        #average service time
        a1= datetime.datetime(2017, 04, 24, begin[0],begin[1],begin[2])
        a2= datetime.datetime(2017, 04, 24, complete[0],complete[1],complete[2])
        sum_s+=dateDiffInSeconds(a1,a2)

        #average wait time
        w1= datetime.datetime(2017, 04, 24, arrival[0],arrival[1],arrival[2])
        w2= datetime.datetime(2017, 04, 24, begin[0],begin[1],begin[2])
        sum_w+=dateDiffInSeconds(w1,w2)
        numOfArrival+=1


        

        #W time spent in system
        W_1= datetime.datetime(2017, 04, 24, arrival[0],arrival[1],arrival[2])
        W_2= datetime.datetime(2017, 04, 24, complete[0],complete[1],complete[2])
        sum_W+=(dateDiffInSeconds(W_1,W_2)/60.0)
        w_list.append(dateDiffInSeconds(W_1,W_2)/60.0)
        


filename= "April19.txt"
with open(filename,'r') as fp:
    d1= fp.readline()
    d2= fp.readline()
    d3= fp.readline()
    d4= fp.readline()
    d5= fp.readline()
    
    From, timeFrom= d3.split(" ")
    start= [int(i) for i in timeFrom.split(":")]
    To, timeTo= d4.split(" ")
    end= [int(i) for i in timeTo.split(":")]
    st= datetime.datetime(2017, 04,24, start[0], start[1], start[2])
    en= datetime.datetime(2017, 04,24, end[0], end[1], end[2])
    dif= dateDiffInSeconds(st, en)
   
    sum_s=0
    sum_w=0
    numOfArrival=0
    for line in fp:
        No_customer, Arrival, Begin, Completion= line.split(" ")
        
        arrival = [int(n) for n in Arrival.split(":")]
        begin =[int(n) for n in Begin.split(":")]
        complete =[int(n) for n in Completion.split(":")]

        #Ws
        Ws1= datetime.datetime(2017, 04, 24, begin[0],begin[1],begin[2])
        Ws2= datetime.datetime(2017, 04, 24, complete[0],complete[1],complete[2])
        Ws.append(dateDiffInSeconds(Ws1, Ws2)/60.0)

        #Wq
        WQ1= datetime.datetime(2017, 04, 24, arrival[0],arrival[1],arrival[2])
        WQ2= datetime.datetime(2017, 04, 24, begin[0],begin[1],begin[2])
        Wq.append(dateDiffInSeconds(WQ1, WQ2)/60.0)

        #waiting Time
        t1= datetime.datetime(2017, 04, 24, arrival[0],arrival[1],arrival[2])
        t2= datetime.datetime(2017, 04, 24, begin[0],begin[1],begin[2])
        all_arrival.append(t1)
        
        #service time
        s1= datetime.datetime(2017, 04, 24, begin[0],begin[1],begin[2])
        s2= datetime.datetime(2017, 04, 24, complete[0],complete[1],complete[2])
        ES.append(dateDiffInSeconds(s1, s2)/60.0)
        
        #average service time
        a1= datetime.datetime(2017, 04, 24, begin[0],begin[1],begin[2])
        a2= datetime.datetime(2017, 04, 24, complete[0],complete[1],complete[2])
        sum_s+=dateDiffInSeconds(a1,a2)

        #average wait time
        w1= datetime.datetime(2017, 04, 24, arrival[0],arrival[1],arrival[2])
        w2= datetime.datetime(2017, 04, 24, begin[0],begin[1],begin[2])
        sum_w+=dateDiffInSeconds(w1,w2)
        numOfArrival+=1


        
        #W time spent in system
        W_1= datetime.datetime(2017, 04, 24, arrival[0],arrival[1],arrival[2])
        W_2= datetime.datetime(2017, 04, 24, complete[0],complete[1],complete[2])
        sum_W+=(dateDiffInSeconds(W_1,W_2)/60.0)
        w_list.append(dateDiffInSeconds(W_1,W_2)/60.0)
        



filename= "April16.txt"
with open(filename,'r') as fp:
    d1= fp.readline()
    d2= fp.readline()
    d3= fp.readline()
    d4= fp.readline()
    d5= fp.readline()
    
    From, timeFrom= d3.split(" ")
    start= [int(i) for i in timeFrom.split(":")]
    To, timeTo= d4.split(" ")
    end= [int(i) for i in timeTo.split(":")]
    st= datetime.datetime(2017, 04,24, start[0], start[1], start[2])
    en= datetime.datetime(2017, 04,24, end[0], end[1], end[2])
    dif= dateDiffInSeconds(st, en)
   
    sum_s=0
    sum_w=0
    numOfArrival=0
    for line in fp:
        No_customer, Arrival, Begin, Completion= line.split(" ")
        
        arrival = [int(n) for n in Arrival.split(":")]
        begin =[int(n) for n in Begin.split(":")]
        complete =[int(n) for n in Completion.split(":")]

        #Ws
        Ws1= datetime.datetime(2017, 04, 24, begin[0],begin[1],begin[2])
        Ws2= datetime.datetime(2017, 04, 24, complete[0],complete[1],complete[2])
        Ws.append(dateDiffInSeconds(Ws1, Ws2)/60.0)

        #Wq
        WQ1= datetime.datetime(2017, 04, 24, arrival[0],arrival[1],arrival[2])
        WQ2= datetime.datetime(2017, 04, 24, begin[0],begin[1],begin[2])
        Wq.append(dateDiffInSeconds(WQ1, WQ2)/60.0)

        #waiting Time
        t1= datetime.datetime(2017, 04, 24, arrival[0],arrival[1],arrival[2])
        t2= datetime.datetime(2017, 04, 24, begin[0],begin[1],begin[2])
        all_arrival.append(t1)
        
        #service time
        s1= datetime.datetime(2017, 04, 24, begin[0],begin[1],begin[2])
        s2= datetime.datetime(2017, 04, 24, complete[0],complete[1],complete[2])
        ES.append(dateDiffInSeconds(s1, s2)/60.0)
        
        #average service time
        a1= datetime.datetime(2017, 04, 24, begin[0],begin[1],begin[2])
        a2= datetime.datetime(2017, 04, 24, complete[0],complete[1],complete[2])
        sum_s+=dateDiffInSeconds(a1,a2)

        #average wait time
        w1= datetime.datetime(2017, 04, 24, arrival[0],arrival[1],arrival[2])
        w2= datetime.datetime(2017, 04, 24, begin[0],begin[1],begin[2])
        sum_w+=dateDiffInSeconds(w1,w2)
        numOfArrival+=1

        #W time spent in system
        W_1= datetime.datetime(2017, 04, 24, arrival[0],arrival[1],arrival[2])
        W_2= datetime.datetime(2017, 04, 24, complete[0],complete[1],complete[2])
        sum_W+=(dateDiffInSeconds(W_1,W_2)/60.0)
        w_list.append(dateDiffInSeconds(W_1,W_2)/60.0)


filename= "April18.txt"
with open(filename,'r') as fp:
    d1= fp.readline()
    d2= fp.readline()
    d3= fp.readline()
    d4= fp.readline()
    d5= fp.readline()
    
    From, timeFrom= d3.split(" ")
    start= [int(i) for i in timeFrom.split(":")]
    To, timeTo= d4.split(" ")
    end= [int(i) for i in timeTo.split(":")]
    st= datetime.datetime(2017, 04,24, start[0], start[1], start[2])
    en= datetime.datetime(2017, 04,24, end[0], end[1], end[2])
    dif= dateDiffInSeconds(st, en)
   
    sum_s=0
    sum_w=0
    numOfArrival=0
    for line in fp:
        No_customer, Arrival, Begin, Completion= line.split(" ")
        
        arrival = [int(n) for n in Arrival.split(":")]
        begin =[int(n) for n in Begin.split(":")]
        complete =[int(n) for n in Completion.split(":")]

        #Ws
        Ws1= datetime.datetime(2017, 04, 24, begin[0],begin[1],begin[2])
        Ws2= datetime.datetime(2017, 04, 24, complete[0],complete[1],complete[2])
        Ws.append(dateDiffInSeconds(Ws1, Ws2)/60.0)

        #Wq
        WQ1= datetime.datetime(2017, 04, 24, arrival[0],arrival[1],arrival[2])
        WQ2= datetime.datetime(2017, 04, 24, begin[0],begin[1],begin[2])
        Wq.append(dateDiffInSeconds(WQ1, WQ2)/60.0)

        #waiting Time
        t1= datetime.datetime(2017, 04, 24, arrival[0],arrival[1],arrival[2])
        t2= datetime.datetime(2017, 04, 24, begin[0],begin[1],begin[2])
        all_arrival.append(t1)
        
        #service time
        s1= datetime.datetime(2017, 04, 24, begin[0],begin[1],begin[2])
        s2= datetime.datetime(2017, 04, 24, complete[0],complete[1],complete[2])
        ES.append(dateDiffInSeconds(s1, s2)/60.0)
        
        #average service time
        a1= datetime.datetime(2017, 04, 24, begin[0],begin[1],begin[2])
        a2= datetime.datetime(2017, 04, 24, complete[0],complete[1],complete[2])
        sum_s+=dateDiffInSeconds(a1,a2)

        #average wait time
        w1= datetime.datetime(2017, 04, 24, arrival[0],arrival[1],arrival[2])
        w2= datetime.datetime(2017, 04, 24, begin[0],begin[1],begin[2])
        sum_w+=dateDiffInSeconds(w1,w2)
        numOfArrival+=1

        
        #W time spent in system
        W_1= datetime.datetime(2017, 04, 24, arrival[0],arrival[1],arrival[2])
        W_2= datetime.datetime(2017, 04, 24, complete[0],complete[1],complete[2])
        sum_W+=(dateDiffInSeconds(W_1,W_2)/60.0)
        w_list.append(dateDiffInSeconds(W_1,W_2)/60.0)



filename= "April25.txt"
with open(filename,'r') as fp:
    d1= fp.readline()
    d2= fp.readline()
    d3= fp.readline()
    d4= fp.readline()
    d5= fp.readline()
   
    sum_s=0
    sum_w=0
    numOfArrival=0
    for line in fp:
        No_customer, Arrival, Begin, Completion= line.split(" ")
        
        arrival = [int(n) for n in Arrival.split(":")]
        begin =[int(n) for n in Begin.split(":")]
        complete =[int(n) for n in Completion.split(":")]

        #Ws
        Ws1= datetime.datetime(2017, 04, 24, begin[0],begin[1],begin[2])
        Ws2= datetime.datetime(2017, 04, 24, complete[0],complete[1],complete[2])
        Ws.append(dateDiffInSeconds(Ws1, Ws2)/60.0)

        #Wq
        WQ1= datetime.datetime(2017, 04, 24, arrival[0],arrival[1],arrival[2])
        WQ2= datetime.datetime(2017, 04, 24, begin[0],begin[1],begin[2])
        Wq.append(dateDiffInSeconds(WQ1, WQ2)/60.0)

        #waiting Time
        t1= datetime.datetime(2017, 04, 24, arrival[0],arrival[1],arrival[2])
        t2= datetime.datetime(2017, 04, 24, begin[0],begin[1],begin[2])
        all_arrival.append(t1)
        
        #service time
        s1= datetime.datetime(2017, 04, 24, begin[0],begin[1],begin[2])
        s2= datetime.datetime(2017, 04, 24, complete[0],complete[1],complete[2])
        ES.append(dateDiffInSeconds(s1, s2)/60.0)
        
        #average service time
        a1= datetime.datetime(2017, 04, 24, begin[0],begin[1],begin[2])
        a2= datetime.datetime(2017, 04, 24, complete[0],complete[1],complete[2])
        sum_s+=dateDiffInSeconds(a1,a2)

        #average wait time
        w1= datetime.datetime(2017, 04, 24, arrival[0],arrival[1],arrival[2])
        w2= datetime.datetime(2017, 04, 24, begin[0],begin[1],begin[2])
        sum_w+=dateDiffInSeconds(w1,w2)
        numOfArrival+=1

        #W time spent in system
        W_1= datetime.datetime(2017, 04, 24, arrival[0],arrival[1],arrival[2])
        W_2= datetime.datetime(2017, 04, 24, complete[0],complete[1],complete[2])
        sum_W+=(dateDiffInSeconds(W_1,W_2)/60.0)
        w_list.append(dateDiffInSeconds(W_1,W_2)/60.0)

filename= "April26.txt"
with open(filename,'r') as fp:
    d1= fp.readline()
    d2= fp.readline()
    d3= fp.readline()
    d4= fp.readline()
    d5= fp.readline()
   
    sum_s=0
    sum_w=0
    numOfArrival=0
    for line in fp:
        No_customer, Arrival, Begin, Completion= line.split(" ")
        
        arrival = [int(n) for n in Arrival.split(":")]
        begin =[int(n) for n in Begin.split(":")]
        complete =[int(n) for n in Completion.split(":")]

        #Ws
        Ws1= datetime.datetime(2017, 04, 24, begin[0],begin[1],begin[2])
        Ws2= datetime.datetime(2017, 04, 24, complete[0],complete[1],complete[2])
        Ws.append(dateDiffInSeconds(Ws1, Ws2)/60.0)

        #Wq
        WQ1= datetime.datetime(2017, 04, 24, arrival[0],arrival[1],arrival[2])
        WQ2= datetime.datetime(2017, 04, 24, begin[0],begin[1],begin[2])
        Wq.append(dateDiffInSeconds(WQ1, WQ2)/60.0)

        #waiting Time
        t1= datetime.datetime(2017, 04, 24, arrival[0],arrival[1],arrival[2])
        t2= datetime.datetime(2017, 04, 24, begin[0],begin[1],begin[2])
        all_arrival.append(t1)
        
        #service time
        s1= datetime.datetime(2017, 04, 24, begin[0],begin[1],begin[2])
        s2= datetime.datetime(2017, 04, 24, complete[0],complete[1],complete[2])
        ES.append(dateDiffInSeconds(s1, s2)/60.0)
        
        #average service time
        a1= datetime.datetime(2017, 04, 24, begin[0],begin[1],begin[2])
        a2= datetime.datetime(2017, 04, 24, complete[0],complete[1],complete[2])
        sum_s+=dateDiffInSeconds(a1,a2)

        #average wait time
        w1= datetime.datetime(2017, 04, 24, arrival[0],arrival[1],arrival[2])
        w2= datetime.datetime(2017, 04, 24, begin[0],begin[1],begin[2])
        sum_w+=dateDiffInSeconds(w1,w2)
        numOfArrival+=1

        #W time spent in system
        W_1= datetime.datetime(2017, 04, 24, arrival[0],arrival[1],arrival[2])
        W_2= datetime.datetime(2017, 04, 24, complete[0],complete[1],complete[2])
        sum_W+=(dateDiffInSeconds(W_1,W_2)/60.0)
        w_list.append(dateDiffInSeconds(W_1,W_2)/60.0)


filename= "April27.txt"
with open(filename,'r') as fp:
    d1= fp.readline()
    d2= fp.readline()
    d3= fp.readline()
    d4= fp.readline()
    d5= fp.readline()
   
    sum_s=0
    sum_w=0
    numOfArrival=0
    for line in fp:
        No_customer, Arrival, Begin, Completion= line.split(" ")
        
        arrival = [int(n) for n in Arrival.split(":")]
        begin =[int(n) for n in Begin.split(":")]
        complete =[int(n) for n in Completion.split(":")]

        #Ws
        Ws1= datetime.datetime(2017, 04, 24, begin[0],begin[1],begin[2])
        Ws2= datetime.datetime(2017, 04, 24, complete[0],complete[1],complete[2])
        Ws.append(dateDiffInSeconds(Ws1, Ws2)/60.0)

        #Wq
        WQ1= datetime.datetime(2017, 04, 24, arrival[0],arrival[1],arrival[2])
        WQ2= datetime.datetime(2017, 04, 24, begin[0],begin[1],begin[2])
        Wq.append(dateDiffInSeconds(WQ1, WQ2)/60.0)

        #waiting Time
        t1= datetime.datetime(2017, 04, 24, arrival[0],arrival[1],arrival[2])
        t2= datetime.datetime(2017, 04, 24, begin[0],begin[1],begin[2])
        all_arrival.append(t1)
        
        #service time
        s1= datetime.datetime(2017, 04, 24, begin[0],begin[1],begin[2])
        s2= datetime.datetime(2017, 04, 24, complete[0],complete[1],complete[2])
        ES.append(dateDiffInSeconds(s1, s2)/60.0)
        
        #average service time
        a1= datetime.datetime(2017, 04, 24, begin[0],begin[1],begin[2])
        a2= datetime.datetime(2017, 04, 24, complete[0],complete[1],complete[2])
        sum_s+=dateDiffInSeconds(a1,a2)

        #average wait time
        w1= datetime.datetime(2017, 04, 24, arrival[0],arrival[1],arrival[2])
        w2= datetime.datetime(2017, 04, 24, begin[0],begin[1],begin[2])
        sum_w+=dateDiffInSeconds(w1,w2)
        numOfArrival+=1

        #W time spent in system
        W_1= datetime.datetime(2017, 04, 24, arrival[0],arrival[1],arrival[2])
        W_2= datetime.datetime(2017, 04, 24, complete[0],complete[1],complete[2])
        sum_W+=(dateDiffInSeconds(W_1,W_2)/60.0)
        w_list.append(dateDiffInSeconds(W_1,W_2)/60.0)


filename= "April28.txt"
with open(filename,'r') as fp:
    d1= fp.readline()
    d2= fp.readline()
    d3= fp.readline()
    d4= fp.readline()
    d5= fp.readline()
   
    sum_s=0
    sum_w=0
    numOfArrival=0
    for line in fp:
        No_customer, Arrival, Begin, Completion= line.split(" ")
        
        arrival = [int(n) for n in Arrival.split(":")]
        begin =[int(n) for n in Begin.split(":")]
        complete =[int(n) for n in Completion.split(":")]

        #Ws
        Ws1= datetime.datetime(2017, 04, 24, begin[0],begin[1],begin[2])
        Ws2= datetime.datetime(2017, 04, 24, complete[0],complete[1],complete[2])
        Ws.append(dateDiffInSeconds(Ws1, Ws2)/60.0)

        #Wq
        WQ1= datetime.datetime(2017, 04, 24, arrival[0],arrival[1],arrival[2])
        WQ2= datetime.datetime(2017, 04, 24, begin[0],begin[1],begin[2])
        Wq.append(dateDiffInSeconds(WQ1, WQ2)/60.0)

        #waiting Time
        t1= datetime.datetime(2017, 04, 24, arrival[0],arrival[1],arrival[2])
        t2= datetime.datetime(2017, 04, 24, begin[0],begin[1],begin[2])
        all_arrival.append(t1)
        
        #service time
        s1= datetime.datetime(2017, 04, 24, begin[0],begin[1],begin[2])
        s2= datetime.datetime(2017, 04, 24, complete[0],complete[1],complete[2])
        ES.append(dateDiffInSeconds(s1, s2)/60.0)
        
        #average service time
        a1= datetime.datetime(2017, 04, 24, begin[0],begin[1],begin[2])
        a2= datetime.datetime(2017, 04, 24, complete[0],complete[1],complete[2])
        sum_s+=dateDiffInSeconds(a1,a2)

        #average wait time
        w1= datetime.datetime(2017, 04, 24, arrival[0],arrival[1],arrival[2])
        w2= datetime.datetime(2017, 04, 24, begin[0],begin[1],begin[2])
        sum_w+=dateDiffInSeconds(w1,w2)
        numOfArrival+=1

        #W time spent in system
        W_1= datetime.datetime(2017, 04, 24, arrival[0],arrival[1],arrival[2])
        W_2= datetime.datetime(2017, 04, 24, complete[0],complete[1],complete[2])
        sum_W+=(dateDiffInSeconds(W_1,W_2)/60.0)
        w_list.append(dateDiffInSeconds(W_1,W_2)/60.0)



for n in range(len(ES)):
    print "{0}. E(Service time): {1}".format(n+1,ES[n])


inter_arr =[]
for i in range(len(all_arrival)-1):
    d= (all_arrival[i+1]-all_arrival[i]).total_seconds()
    if d>0:
        inter_arr.append(d/60.0)
print "--inter-arrival time--"
for n in range(len(inter_arr)):
    print n+1 ,inter_arr[n]
print np.mean(inter_arr)
print len(inter_arr)



for n in range(len(w_list)):
    print n, w_list[n], "min"
print "-sum of all W-"
print sum_W
print "-AVG of W-"
print sum_W/214.0

print""
print "--WQ--"
print np.mean(Wq)

print""
print "--WS--"
print np.mean(Ws)

    



