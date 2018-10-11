import math
import numpy as np



def DividedDifferences(x,a):
	n = len(x)
	n = n-1
	F = [[np.float64(0) for x in range(n+1)] for y in range(n+1)] 
	for(i) in range(0,n+1):
		F[i][0] = a[i]


	for i in range(1,n+1):
		for j in range(1,i+1):
			F[i][j] = (F[i][j-1] - F[i-1][j-1]) / (x[i]-x[i-j])

	return F

