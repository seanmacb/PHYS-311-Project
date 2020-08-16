#Sean MacBride 
#7 Febuary 2018 
#A code to solve the differential equation x'' = g -kx'
#PLEASE SEE CONCLUSIONS AT THE BOTTOM OF THIS PROGRAM
import matplotlib.pyplot as plt
import math
# Global variables
g=9.8
k=0.7
h=0.01
hval="h="+str(h)
def motion():
    vold=0
    told=0
    xold=0
    xlist=[]
    tlist=[]
    vlist=[]
    tlist.append(told)
    vlist.append(vold)
    xlist.append(xold)
    for i in range (1,int(10/h)):
        tnew=told+h
        xnew=xold+vold*h
        vnew=vold+h*(g-k*vold)
        tnew=told+h
        tlist.append(tnew)
        vlist.append(vnew)
        xlist.append(xnew)
        vold=vnew
        told=tnew
    plt.plot(tlist,vlist)
    plt.xlabel('Time (s)')
    plt.ylabel('Velocity (m/s)')
    plt.text(8, 16, hval,fontsize=12)
    plt.savefig("terminalvelocity_sean_macbride.png")
    plt.show()
motion()
#EVERYTHING BELOW IS A WORK IN PROGRESS
'''
def error():
    vold=0
    told=0
    xold=0
    errold=0
    xlist=[]
    tlist=[]
    vlist=[]
    errlist=[]
    vanallist=[]
    errlist.append(errold)
    tlist.append(told)
    vlist.append(vold)
    xlist.append(xold)
    for i in range (1,int(10/h)):
        tnew=told+h
        xnew=xold+vold*h
        vnew=vold+h*(g-k*vold)
        tnew=told+h
        tlist.append(tnew)
        vlist.append(vnew)
        xlist.append(xnew)
        vold=vnew
        told=tnew
        vanal=(g/k)*(1-math.exp(-k*tnew))
        errnew=math.fabs(100*((vnew)/(vanal)-1))
        errlist.append(errnew)
    plt.plot(tlist,errlist)
    plt.xlabel('Time (s)')
    plt.ylabel('Percent Error (%)')
    plt.text(8, 1, hval,fontsize=12)
    plt.savefig("ode2_sean_macbride.png")
    plt.show()     
error()
'''
'''
Conclusions:
Was able to successfully solve the equation for Q4
Was able to successfully plot graph required for Q5
Was able to successfully plot graph required for Q6
For Q7 I found that h=0.04 yielded around a maximum of 1% error
'''