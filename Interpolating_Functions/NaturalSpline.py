import math
import numpy as np

def NaturalSpline(n,x,a):
	i=0
	h = [np.float128(0.0)] * n
	while i <= n-2:
		#print(i)
		h[i] = x[i+1] - x[i]
		i=i+1
		#print(h[i])

	i=1
	alpha = [np.float128(0.0)] * n
	while i<=n-2:
		alpha[i] = ((3/h[i])*(a[i+1]-a[i])) - ((3/h[i-1])*(a[i]-a[i-1]))
		i=i+1

	l = [np.float128(0.0)] * n
	miu = [np.float128(0.0)] * n
	z = [np.float128(0.0)] * n

	l[0] = 1
	miu[0] = 0
	z[0] = 0

	i=1
	while i <= n-2:
		l[i] = (2*(x[i+1] - x[i-1])) - (h[i-1]*miu[i-1])
		miu[i] = h[i]/l[i]
		z[i] = (alpha[i] - (h[i-1]*z[i-1]))/l[i]
		i=i+1

	c = [np.float128(0.0)] * n
	l[n-1] = 1
	z[n-1] = 0
	c[n-1] = 0

	b = [np.float128(0.0)] * n
	d = [np.float128(0.0)] * n

	j = n-2
	while j!=-1:
		c[j] = z[j] - (miu[j]*c[j+1])
		b[j] = ((a[j+1]-a[j])/h[j])-h[j]*(c[j+1]+2*c[j])/3
		d[j] = (c[j+1]-c[j])/(3*h[j])
		j = j-1

	return a,b,c,d
	