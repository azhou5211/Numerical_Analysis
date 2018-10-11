import math


#Type your function here:
def f(x):
	y = x**2 - 4*x + 4 - math.log(x)
	return y
# a,b are starting positions
a = 1.0
b = 2.0
#change epsilon to adjust error size
epsilon = 0.0000000001

if (f(a) * f(b)) >= 0:
	print("invalid interval")
	quit()


error = 1.0
count = 0
while (error > epsilon):
	count = count+1
	c = (a+b)/2
	error = b-c
	func = f(c)
	if f(a)<0 and f(b)>0:
		if func == 0:
			break
		elif func > 0:
			b = c
		else:
			a = c
	else:
		if func == 0:
			break
		elif func > 0:
			a = c
		else:
			b = c
	print("n=",count,"a=",a,"b=",b,"c=",c,"error=",error,"f(x)=",func)

