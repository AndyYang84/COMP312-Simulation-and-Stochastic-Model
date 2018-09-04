import datetime, time
def dateDiffInSeconds(date1, date2):
    time_delta = date2 - date1
    return time_delta.days*24*3600 + time_delta.seconds

with open("April17.txt",'r') as fp:
    d1= fp.readline()
    d2= fp.readline()
    d3= fp.readline()
    d4= fp.readline()+"Date:17, April lunch\nWait= Service Begin-Arrival time\nService time= Service completion- Service Begin\n"
    d5= fp.readline()
    
    print d1,d2,d3,d4,d5
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

        #expected service time
        a1= datetime.datetime(2017, 04, 17, begin[0],begin[1],begin[2])
        a2= datetime.datetime(2017, 04, 17, complete[0],complete[1],complete[2])
        sum_s+=dateDiffInSeconds(a1,a2)

        #expected wait time
        w1= datetime.datetime(2017, 04, 17, arrival[0],arrival[1],arrival[2])
        w2= datetime.datetime(2017, 04, 17, begin[0],begin[1],begin[2])
        sum_w+=dateDiffInSeconds(w1,w2)

print "Average expected service time E(S)= ", (sum_s/(23.0)), "sec ({0}min)".format( (sum_s/(23.0))/60.0)
print "Average waiting time= ", (sum_w/(23.0)), "sec ({0}min)".format((sum_w/(23.0))/60.0)
print "++++++++++++++++++++++++++++++++++++++++++++++++++++++++++"

with open("April24.txt",'r') as fp:
    d1= fp.readline()
    d2= fp.readline()
    d3= fp.readline()
    d4= fp.readline()+"Date:24, April lunch\nWait= Service Begin-Arrival time\nService time= Service completion- Service Begin\n"
    d5= fp.readline()
    
    print d1,d2,d3,d4,d5
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

        #expected service time
        a1= datetime.datetime(2017, 04, 24, begin[0],begin[1],begin[2])
        a2= datetime.datetime(2017, 04, 24, complete[0],complete[1],complete[2])
        sum_s+=dateDiffInSeconds(a1,a2)

        #expected wait time
        w1= datetime.datetime(2017, 04, 24, arrival[0],arrival[1],arrival[2])
        w2= datetime.datetime(2017, 04, 24, begin[0],begin[1],begin[2])
        sum_w+=dateDiffInSeconds(w1,w2)

print "Average expected service time E(S)= ", (sum_s/(28.0)), "sec ({0}min)".format( (sum_s/(28.0))/60.0)
print "Average waiting time= ", (sum_w/(28.0)), "sec ({0}min)".format((sum_w/(28.0))/60.0)

