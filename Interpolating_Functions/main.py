import math
import numpy as np
import sys
from DividedDifferences import DividedDifferences
from NaturalSpline import NaturalSpline
import matplotlib.pyplot as plt

#Enter the number of points into n. (Not array length)
n=21
x = [0.9,1.3,1.9,2.1,2.6,3.0,3.9,4.4,4.7,5.0,6.0,7.0,8.0,9.2,10.5,11.3,11.6,12.0,12.6,13.0,13.3]
a = [1.3,1.5,1.85,2.1,2.6,2.7,2.4,2.15,2.05,2.1,2.25,2.3,2.25,1.95,1.4,0.9,0.7,0.6,0.5,0.4,0.25]

if (n<2):
	print("Need more than one point, cannot run")
	sys.exit()


#Cubic Spline
a,b,c,d = NaturalSpline(n,x,a)
print("Coefficients for Natural Cubic Spline")
for j in range(0,n-1):
	print("j = %d, a: %f, b: %f, c: %f, d: %f" % (j,a[j],b[j],c[j],d[j]))

#Divided Difference
ans = DividedDifferences(x,a)
print("Coefficients for interpolating polynomial")
for i in range(0,n):
	print("F[%d,%d] = %f" % (i,i,ans[i][i]))

#Plotting the Cubic Spline
for i in range(0,n-1):
	k = np.linspace(x[i],x[i+1],200,endpoint=True)
	y = a[i] + b[i]*(k-x[i]) + c[i]*((k-x[i])**2) + d[i]*((k-x[i])**3)
	plt.plot(k,y,'b')

#Plotting the Divided Difference
k = np.linspace(x[0],x[n-1],1000)
y = ans[0][0]
for i in range(1,n):
	temp = ans[i][i]
	j = 0
	while(j<i):
		temp = temp*(k-x[j])
		j=j+1
	y = y + temp
plt.plot(k,y,'k')

#Plotting the original points
plt.plot(x,a,'ro')
plt.show()
