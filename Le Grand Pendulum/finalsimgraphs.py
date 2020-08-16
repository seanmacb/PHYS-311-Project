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
    if (xposlist[i] < 182):
        theta = -theta
    theta = (theta*360)/(2*math.pi)
    thetatlist.append(theta)



tlast20list=tlist[-101:len(tlist)-1]#last 20 second time stamps
tfirst20list=tlist[:101]#first 20 second time stamps
thetalast20list=thetatlist[-101:len(thetatlist)-1]
thetafirst20list=thetatlist[:101]


tlist2 = tlist
#-----------------------------** PART 2 **-----------------------------

def thetagraph(tlist,ThetaList):
	plt.plot(tlist,ThetaList)
	plt.xlabel('Time (s)')
	plt.ylabel('Analytical Theta (degrees)')
	plt.show()
	input("Press Enter to continue")
	plt.close()

def thetagraphFirst20(tlistF20,ThetaListF20):
	plt.plot(tlistF20,ThetaListF20)
	plt.xlabel('Time (s)')
	plt.ylabel('Analytical Theta (degrees)')
	plt.show()
	input("Press Enter to continue")
	plt.close() 

def thetagraphLast20(tlistL20,ThetaListL20):
	plt.plot(tlistL20,ThetaListL20)
	plt.xlabel('Time (s)')
	plt.ylabel('Analytical Theta (degrees)')
	plt.show()
	input("Press Enter to continue")
	plt.close()

def thetaLastAnyVsExp(tlistL20,ThetaListL20, AT, Ath):
    plt.plot(tlistL20,ThetaListL20)
    plt.plot(AT,Ath)
    plt.xlabel('Time (s)')
    plt.ylabel('Analytical Vs Experimental Theta (degrees)')
    plt.show() 
    input("Press Enter to continue")
    plt.close()
    
def thetaFirstAnyVsExp(tlistF20,ThetaListF20, AT, Ath):
    plt.plot(tlistF20,ThetaListF20)
    plt.plot(AT,Ath)
    plt.xlabel('Time (s)')
    plt.ylabel('Analytical Vs Experimental Theta (degrees)')
    plt.show() 
    input("Press Enter to continue")
    plt.close() 
    
def thetaAnyVsExp(tlist,Theta, AT, Ath):
    plt.plot(tlist,Theta)
    plt.plot(AT,Ath)
    plt.xlabel('Time (s)')
    plt.ylabel('Analytical Vs Experimental Theta (degrees)')
    plt.show()     
    input("Press Enter to continue")
    plt.close() 
    
def main():
	
	told=0
	ThetaDotOld=0
	ThetaOld=-0.38013
	h=0.2#timestep, decide for yourself
	b=1.479#play with the damping parameter
	n=0.995#play with this too (check sheet)
	l=1.15#length in pixels
	g=9.81976 #local gravity in norton
	omegaknot=math.sqrt(g/l)
	
	Fdrag = 0
	FdragList = []
	FdragList.append(0)
	tlist=[]
	ThetaDotList=[]
	ThetaList=[]
	
	tlist.append(told)
	ThetaDotList.append(ThetaDotOld)
	ThetaList.append(ThetaOld)	
	
	for i in range(int(450/h)):
		Fdrag = ((-b) * (l**n) * abs(ThetaDotOld)**n)
		if (ThetaDotOld < 0):
			Fdrag = -Fdrag		
		
		tnew=told+h
		ThetaDotNew= ThetaDotOld + (h*(Fdrag - (omegaknot**2)*math.sin(ThetaOld)))
		ThetaNew=ThetaOld + h*ThetaDotOld
		
		tlist.append(tnew)
		
		ThetaList.append(ThetaOld*(180/math.pi))
		ThetaDotList.append(ThetaDotNew)
		
		FdragList.append(Fdrag)
		
		told=tnew
		ThetaDotOld=ThetaDotNew
		ThetaOld=ThetaNew
	
	#tlast20list=tlist[-102:len(tlist)-1]#last 20 second time stamps
	#tfirst20list=tlist[:102]#first 20 second time stamps
	#thetalast20list=Thetatlist[-102:len(thetatlist)-1]
	#thetafirst20list=thetatlist[:102]	
	
	AtFirst20 = tlist[:101]
	AtLast20 = tlist[-101:len(tlist)-1]
	
	AThetaLast20 = ThetaList[-101:len(ThetaList)-1]
	AThetaFirst20 = ThetaList[:101]
	
	thetaAnyVsExp(tlist2,thetatlist,tlist,ThetaList)
	
	thetagraph(tlist,ThetaList) 
	
	thetagraphFirst20(AtFirst20,AThetaFirst20)
	
	thetagraphLast20(AtLast20,AThetaLast20)
	
	thetaLastAnyVsExp(AtLast20,thetalast20list, AtLast20, AThetaLast20)
	
	thetaFirstAnyVsExp(AtFirst20,thetafirst20list, AtFirst20, AThetaFirst20)
	
	

main()