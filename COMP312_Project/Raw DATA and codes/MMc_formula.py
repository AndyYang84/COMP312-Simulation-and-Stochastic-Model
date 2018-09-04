
#author:Andy
import random
import numpy
import math
#Theoretical Result from M/M/c formula
"""observed W= 5.9608 minutes
(overall average waiting time for a customerin the system)"""

def MMc(lamb, mu, c):
    rho= lamb/mu
    #get Pi[0]:
    pi0= ((rho**0)/math.factorial(0)+(rho**1)/math.factorial(1)+
          ((rho**c)/math.factorial(c)*(1/(1-rho/c)**2)))**(-1)
    Lq= (rho**c/math.factorial(c)*pi0)*(rho/c/(1-rho/c)**2)
    Ls= rho
    L=Lq+Ls
    W=L/lamb
    print "W=" ,W, "minutes (theoretical result)"
    print "Wq=", Lq/lamb
    print "L=", L
    print "Lq", Lq
    print "π0=", pi0
    print "π1=", pi0*(rho)
    print "π2=", pi0*(rho**2/math.factorial(2))
    print "π3=", pi0*(rho**3/(math.factorial(2)*(2**1)))
    print "π4=", pi0*(rho**4/(math.factorial(2)*(2**2)))
    print "π5=", pi0*(rho**5/(math.factorial(2)*(2**3)))
    print "π6=", pi0*(rho**6/(math.factorial(2)*(2**4)))
    print"λ=", lamb, "(arrival rate)"
    print"Mu=", mu, "(service rate)"
    print"E(S)=", 1/mu, "minutes (expected service time)"
    print "ρ/c =",(rho)/c 
    if (rho/c)<1:
        print "∴ SSD∃"
    else:
        print" >1 ∴SSD not exists"
#Calculate with our observation data results
overall_lamb= 0.215
overall_mu= 0.212336
c=2
MMc(overall_lamb, overall_mu, c)

