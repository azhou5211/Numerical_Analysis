import math

#Type your function here:
def f(x):
	y = math.exp(x) - math.sin(x) - 2
	return y

# a,b are starting positions
a = 1.0
b = 2.0

#Change epsilon to change error size
epsilon = 0.0000000001

error = 1.0
count = 1
current = b
prev = a
while (error > epsilon):
	count = count+1
	fnext = current - f(current)*((current-prev)/(f(current)-f(prev)))
	error = abs(fnext-current)
	prev = current
	current = fnext
	print("n=",count,"xn=",current,"x(n-1)=",prev,"error=",error)
	if(count==1000):
		break
