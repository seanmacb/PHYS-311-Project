import matplotlib.pyplot as plt
import math

xOld=0
yNew=0
yOld=1
xSet=[]
ySet=[]
ySet.append(yOld)
xSet.append(xOld)
g=9.8
h = .1
for i in range (0,101):
    yNew=yOld+(h*(math.sin(xOld)))
    xOld+=h
    yOld=yNew
    xSet.append(xOld)
    ySet.append(yNew) 
print(xSet)
print(ySet)

plt.plot(xSet,ySet)
plt.show()
