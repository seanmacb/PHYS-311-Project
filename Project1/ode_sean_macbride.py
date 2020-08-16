#Sean MacBride 
#7 Febuary 2018 
#A code to solve the differential equation x'' = g 
#Claire hammond and i worked one ODE1, I worked solo on ODE2

import matplotlib.pyplot as plt 

#Global variables
g = 9.8 
h = 0.1



def motion(): 

	vlist = []

	vold = 0
	told= 0
	tlist=[]
	tlist.append(told)
	vlist.append (vold)

	for k in range (1,int(10/h)): 

		vnew = vold + (h * g)
		tnew = told+h
		
		tlist.append(tnew)

		vlist.append(vnew)
		told=tnew
		vold = vnew 
	
	
		
	'''
	
	To view the graph of v versus t, remove the mutli line comment here	
	
	plt.plot(tlist,vlist)
	plt.xlabel('Time (s)')
	plt.ylabel('Velocity (m/s)')
	
	'''
	plt.show()	

	return (vlist) 
	
	#Move the plots to above/below the return to view the plot
	#plt.plot(xlist, ylist)
	#plt.ylabel ("y-direction (height)")
	#plt.xlabel ("x-direction")
	#plt.show()	


#Input: the velocity list 
#Output: A list of the error percentages 

def error(vnum): 

	# These are the starting variables (vana is anlytical velovity, vnum is numerical velocity)
	vana = []
	tlist = []
	t = 0
	told=0

	#This loop creates the analytical

	for k in range (0,int(10/h)): 

		vnew = g*t 

		vana.append(vnew) 

		tlist.append(t)

		t = t + h


	#Error loop

	errorlist = [] 

	for k in range (int(10/h)): 
		print("The numerical velocity is", vnum[k]) 
		print("The analytical velocity is", vana[k])
		if (vana[k] == 0): 
			errorlist.append(0)
		else: 
			perror = 100 * ( (vnum[k] - vana[k])/(vana[k]) )

			errorlist.append(perror)

	print (errorlist)


	return (errorlist, tlist)

def plot (theerror, thetime): 
	
	
	
	hval="h= "+str(h)
	plt.plot(thetime, theerror) 
	plt.xlabel("Time (s)")
	plt.ylabel("Percent error (%)")
	plt.title("Error percentage over time")
	plt.text(9,1.2*10**-13, hval,fontsize=12)
	plt.savefig("ode_sean_macbride.png")
	plt.show()
	


def main():
	listofv = motion()

	errorvalue, time = error (listofv)

	plot(errorvalue, time)



main()  


'''

For Q1, was able to solve the differential equation
For Q2, the graph shows a graph of velocity vs. time and is saved as ode_sean_macbride.png
For Q3, there isn't a value of h that yields a percent error higher than 1%

'''