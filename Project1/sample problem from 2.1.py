#Aim: to make a simple plot
import matplotlib.pyplot as plt
import math
t= [0, 2.9, 3.9, 5.9,8.3]
m= [3.02,2.83,2.83,2.98,3.06]
plt.plot(t,m,'r-', t,m,'g^')

plt.xlabel('Time since 2018 Jan 21 10:54 EST (days)')
plt.ylabel('Olympia\'s mass (kg)')
plt.xlim(-.5,10.5)
plt.ylim(2.8,3.1)
plt.savefig('myplot.png')
plt.close()