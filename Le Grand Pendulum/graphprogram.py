#Sean MacBride and Mo Hayat
#Producing the graphs required for "Le Grand Pendulum" Project

import numpy as np
import matplotlib.pyplot as plt
import math

#Extracting the data

ip="ClassicalProj2Sean+Mo.csv"

tlist = np.genfromtxt(ip, usecols=(0), delimiter=",", skip_header=1)
xposlist = np.genfromtxt(ip, usecols=(1), delimiter=",", skip_header=1)
yposlist = np.genfromtxt(ip, usecols=(2), delimiter=",", skip_header=1)
xvellist = np.genfromtxt(ip, usecols=(3), delimiter=",", skip_header=1)
yvellist = np.genfromtxt(ip, usecols=(4), delimiter=",", skip_header=1)
'''tlast20list=tlist[-102:len(tlist)-1]#last 20 second time stamps
xlast20list=xposlist[-102:len(xposlist)-1]#last 20 seconds worth of x positions
ylast20list=yposlist[-102:len(yposlist)-1]#last 20 seconds worth of y positions
tfirst20list=tlist[:102]#first 20 second time stamps
xfirst20list=xposlist[:102]#first 20 seconds x position stamps
yfirst20list=yposlist[:102]#first 20 seconds y position stamps'''

'''
thetatlist=[]
for i in range(len(tlist)):
    thetaval=np.arccos((xposlist[i]-177)**2+(yposlist[i]-562)**2)/(79202)
    thetatlist.append(thetaval)
tlast20list=tlist[-102:len(tlist)-1]#last 20 second time stamps
tfirst20list=tlist[:102]#first 20 second time stamps
thetalast20list=thetatlist[-102:len(thetatlist)-1]
thetafirst20list=thetatlist[:102]

TRIED MAKING THIS LIST, IT DIDNT WORK. MIGHT BE A BETTER IDEA TO JUST CALCULATE IT IN EXCEL AND EXTRACT IN INTO HERE FROM THERE

''' 

thetatlist=[]

for i in range(len(tlist)): 
    theta = math.acos(1-(((xposlist[i]-182)**2 + (yposlist[i] - 362)**2)/(66284)))  
    # theta = Cos^-1 (1 - (Xi - X0)^2 + (Yi -Y0)^2)/(2b^2)
    if (xposlist[i] < 182):
        theta = -theta
    theta = (theta*360)/(2*math.pi)
    thetatlist.append(theta)

tlast20list=tlist[-101:len(tlist)-1]#last 20 second time stamps
tfirst20list=tlist[:101]#first 20 second time stamps
thetalast20list=thetatlist[-101:len(thetatlist)-1]
thetafirst20list=thetatlist[:101]

def xygraph():
    plt.plot(xposlist,yposlist)
    plt.xlabel("X Position (Pixels)")
    plt.ylabel("Y Position (Pixels)")
    plt.show()
    input("Press <enter> to continue")
    plt.close()
    
def xtimegraph():
    plt.plot(tlist, xposlist)
    plt.xlabel("Time (seconds)")
    plt.ylabel("X Position (Pixels)")
    plt.show()
    input("Press <enter> to continue")
    plt.close()
    
def ytimegraph():
    plt.plot(tlist, yposlist)
    plt.xlabel("Time (seconds)")
    plt.ylabel("Y Position (Pixels)")
    plt.show()
    input("Press <enter> to continue")
    plt.close()
    
    
def thetatall():
    plt.plot(tlist, thetatlist)
    plt.xlabel("Time (seconds)")
    plt.ylabel("Theta(t)")
    plt.show()
    input("Press <enter> to continue")
    plt.close()    
    
def thetalast20():
    plt.plot(tlast20list, thetalast20list)
    plt.xlabel("Time (seconds)")
    plt.ylabel("Theta(t)")
    plt.show()
    input("Press <enter> to continue")
    plt.close()      
    
def thetafirst20():
    plt.plot(tfirst20list, thetafirst20list)
    plt.xlabel("Time (seconds)")
    plt.ylabel("Theta(t)")
    plt.show()
    input("Press <enter> to continue")
    plt.close()      
    
    
#I need you to write the algorithim to graph theta(t) over the intervals. I already have lists up top for the first and last 20 seconds of time, x positions, and y positions
#I'm thinking a for loop to compound the values of theta(t) into a list, and then graphing it once the for loop works correctly
    
    
def main():
    
    prompt=input("Input which graph you want. Valid inputs are xygraph, xtimegraph, ytimegraph, thetatall, thetafirst20, thetalast20, and close. ")
   
   
    while prompt!="close":
        if prompt=="xygraph":
            xygraph()
            prompt=input("Input which graph you want. Valid inputs are xygraph, xtimegraph, ytimegraph, thetatall, thetafirst20, thetalast20, and close. ")
        elif prompt=="xtimegraph":
            xtimegraph()
            prompt=input("Input which graph you want. Valid inputs are xygraph, xtimegraph, ytimegraph, thetatall, thetafirst20, thetalast20, and close. ")
        elif prompt=="ytimegraph":
            ytimegraph()
            prompt=input("Input which graph you want. Valid inputs are xygraph, xtimegraph, ytimegraph, thetatall, thetafirst20, thetalast20, and close. ")
        elif prompt=="thetatall":
            thetatall()
            prompt=input("Input which graph you want. Valid inputs are xygraph, xtimegraph, ytimegraph, thetatall, thetafirst20, thetalast20, and close. ")
        elif prompt=="thetafirst20":
            thetafirst20()
            prompt=input("Input which graph you want. Valid inputs are xygraph, xtimegraph, ytimegraph, thetatall, thetafirst20, thetalast20, and close. ")
        elif prompt=="thetalast20":
            thetalast20()
            prompt=input("Input which graph you want. Valid inputs are xygraph, xtimegraph, ytimegraph, thetatall, thetafirst20, thetalast20, and close. ")
        else:
            print("Incorrect entry, please enter another prompt")
            prompt=input("Input which graph you want. Valid inputs are xygraph, xtimegraph, ytimegraph, thetatall, thetafirst20, thetalast20, and close. ")
    print("Finished!")
main()


#Questions for Hw4

#d x=177 y=562

#e x=182 y=362

#f y=-40x+7642

#g theta(t) = cos^-1 [((x(t)-177)^2 + (y(t) - 562)^2)/(79202)]