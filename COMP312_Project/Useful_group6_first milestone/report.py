import datetime, time
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
print "[ Arrival, Service Begin, Service Completion]"
for n in range(0, Num_observation):
    print n+1, cu[n]
print ""
print "07, Aprial  (26 observations)-Minping"

#Service time
Sum=0
for n in range(0, Num_observation):
    service_time=cu[n][2]- cu[n][1]
    Sum+=service_time
print "E(s)= ", Sum/(Num_observation), "sec  ({0} min)".format((Sum/(Num_observation))/(60.0))

#Wait time
Sum=0
for n in range(0, Num_observation):
    w_time=cu[n][1]- cu[n][0]
    Sum+=w_time
print "E(w)= ", Sum/(Num_observation), "sec  ({0} min)".format((Sum/(Num_observation))/(60.0))
print "____________________________________________"

def dateDiffInSeconds(date1, date2):
    time_delta = date2 - date1
    return time_delta.days*24*3600 + time_delta.seconds

with open("April17.txt",'r') as fp:
    d1= fp.readline()
    d2= fp.readline()
    d3= fp.readline()
    d4= fp.readline()+"Date:17, April lunch\nWait= Service Begin-Arrival time\nService time= Service completion- Service Begin\n"
    d5= fp.readline()
    
    #print d1,d2,d3,d4,d5
    sum_s=0
    sum_w=0
    for line in fp:
        
        No_customer, Arrival, Begin, Completion= line.split(" ")
        
        arrival = [int(n) for n in Arrival.split(":")]
        begin =[int(n) for n in Begin.split(":")]
        complete =[int(n) for n in Completion.split(":")]

        #waiting Time
        t1= datetime.datetime(2017, 04, 17, arrival[0],arrival[1],arrival[2])
        t2= datetime.datetime(2017, 04, 17, begin[0],begin[1],begin[2])
        
        #service time
        s1= datetime.datetime(2017, 04, 17, begin[0],begin[1],begin[2])
        s2= datetime.datetime(2017, 04, 17, complete[0],complete[1],complete[2])
        print "No.",line, "Wait: {0} sec\nService time: {1} sec\n_________________________________".format(dateDiffInSeconds(t1, t2), dateDiffInSeconds(s1, s2))
        """print all records"""

        #expected service time
        a1= datetime.datetime(2017, 04, 17, begin[0],begin[1],begin[2])
        a2= datetime.datetime(2017, 04, 17, complete[0],complete[1],complete[2])
        sum_s+=dateDiffInSeconds(a1,a2)

        #expected wait time
        w1= datetime.datetime(2017, 04, 17, arrival[0],arrival[1],arrival[2])
        w2= datetime.datetime(2017, 04, 17, begin[0],begin[1],begin[2])
        sum_w+=dateDiffInSeconds(w1,w2)
print " "
print "17, April  (23 observations)- Andy"
print "E(S)= ", (sum_s/(23.0)), "sec  ({0} min)".format( (sum_s/(23.0))/60.0)
print "E(w)= ", (sum_w/(23.0)), "sec  ({0} min)".format((sum_w/(23.0))/60.0)
print "____________________________________________"

with open("April24.txt",'r') as fp:
    d1= fp.readline()
    d2= fp.readline()
    d3= fp.readline()
    d4= fp.readline()+"Date:24, April lunch\nWait= Service Begin-Arrival time\nService time= Service completion- Service Begin\n"
    d5= fp.readline()
    
    #print d1,d2,d3,d4,d5
    sum_s=0
    sum_w=0
    for line in fp:
        No_customer, Arrival, Begin, Completion= line.split(" ")
        
        arrival = [int(n) for n in Arrival.split(":")]
        begin =[int(n) for n in Begin.split(":")]
        complete =[int(n) for n in Completion.split(":")]

        #waiting Time
        t1= datetime.datetime(2017, 04, 24, arrival[0],arrival[1],arrival[2])
        t2= datetime.datetime(2017, 04, 24, begin[0],begin[1],begin[2])
        
        #service time
        s1= datetime.datetime(2017, 04, 24, begin[0],begin[1],begin[2])
        s2= datetime.datetime(2017, 04, 24, complete[0],complete[1],complete[2])
        print "No.",line, "Wait: {0} sec\nService time: {1} sec\n_________________________________".format(dateDiffInSeconds(t1, t2), dateDiffInSeconds(s1, s2))
        """print all records"""
        #expected service time
        a1= datetime.datetime(2017, 04, 24, begin[0],begin[1],begin[2])
        a2= datetime.datetime(2017, 04, 24, complete[0],complete[1],complete[2])
        sum_s+=dateDiffInSeconds(a1,a2)

        #expected wait time
        w1= datetime.datetime(2017, 04, 24, arrival[0],arrival[1],arrival[2])
        w2= datetime.datetime(2017, 04, 24, begin[0],begin[1],begin[2])
        sum_w+=dateDiffInSeconds(w1,w2)
print " "
print "24, April  (28 observations)- Andy"
print "E(S)= ", (sum_s/(28.0)), "sec  ({0} min)".format( (sum_s/(28.0))/60.0)
print "E(w)= ", (sum_w/(28.0)), "sec  ({0} min)".format((sum_w/(28.0))/60.0)

print "____________________________________________"

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
print "[ Arrival, Service Begin, Service Completion]"
for n in range(0, Num_observation):
    print n+1, cu[n]
print ""

print "14, Aprial  (8 observations)- Haochen"

#Service time
Sum=0
for n in range(0, Num_observation):
    service_time=cu[n][2]- cu[n][1]
    Sum+=service_time
print "E(s)= ", Sum/(Num_observation), "sec  ({0} min)".format((Sum/(Num_observation))/(60.0))

#Wait time
Sum=0
for n in range(0, Num_observation):
    w_time=cu[n][1]- cu[n][0]
    Sum+=w_time
print "E(w)= ", Sum/(Num_observation), "sec  ({0} min)".format((Sum/(Num_observation))/(60.0))


print "____________________________________________"

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
print "[ Arrival, Service Begin, Service Completion]"
for n in range(0, Num_observation):
    print n+1, cu[n]
print ""
print "21, Aprial  (30 observations)- Mark"

#Service time
Sum=0
for n in range(0, Num_observation):
    service_time=cu[n][2]- cu[n][1]
    Sum+=service_time
print "E(s)= ", Sum/(Num_observation), "sec  ({0} min)".format((Sum/(Num_observation))/(60.0))

#Wait time
Sum=0
for n in range(0, Num_observation):
    w_time=cu[n][1]- cu[n][0]
    Sum+=w_time
print "E(w)= ", Sum/(Num_observation), "sec  ({0} min)".format((Sum/(Num_observation))/(60.0))
        

print "____________________________________________"

with open("April18.txt",'r') as fp:
    d1= fp.readline()
    d2= fp.readline()
    d3= fp.readline()
    d4= fp.readline()+"Date:18, April lunch\nWait= Service Begin-Arrival time\nService time= Service completion- Service Begin\n"
    d5= fp.readline()
    
    #print d1,d2,d3,d4,d5
    sum_s=0
    sum_w=0
    for line in fp:
        No_customer, Arrival, Begin, Completion= line.split(" ")
        
        arrival = [int(n) for n in Arrival.split(":")]
        begin =[int(n) for n in Begin.split(":")]
        complete =[int(n) for n in Completion.split(":")]

        #waiting Time
        t1= datetime.datetime(2017, 04, 18, arrival[0],arrival[1],arrival[2])
        t2= datetime.datetime(2017, 04, 18, begin[0],begin[1],begin[2])
        
        #service time
        s1= datetime.datetime(2017, 04, 18, begin[0],begin[1],begin[2])
        s2= datetime.datetime(2017, 04, 18, complete[0],complete[1],complete[2])
        print "No.",line, "Wait: {0} sec\nService time: {1} sec\n_________________________________".format(dateDiffInSeconds(t1, t2), dateDiffInSeconds(s1, s2))
        """print all records"""
        #expected service time
        a1= datetime.datetime(2017, 04, 18, begin[0],begin[1],begin[2])
        a2= datetime.datetime(2017, 04, 18, complete[0],complete[1],complete[2])
        sum_s+=dateDiffInSeconds(a1,a2)

        #expected wait time
        w1= datetime.datetime(2017, 04, 18, arrival[0],arrival[1],arrival[2])
        w2= datetime.datetime(2017, 04, 18, begin[0],begin[1],begin[2])
        sum_w+=dateDiffInSeconds(w1,w2)
print " "
print "18, April  (25 observations)- Andy"
print "E(S)= ", (sum_s/(25.00)), "sec  ({0} min)".format( (sum_s/(25.0))/60.0)
print "E(w)= ", (sum_w/(25.00)), "sec  ({0} min)".format((sum_w/(25.0))/60.0)

print "____________________________________________"

