import math

#Type your function and derivative function here:
def f(x): #function
	y = math.exp(x) - x -1
	return y
def derf(x): #derivative
	y = math.exp(x) -1
	return y

# a is starting position (x0). Change a to change starting position.
a = 1.0

#Change epsilon to change error size
epsilon = 0.0000000001

function = f(a)
derv = derf(a)
x = a - function/derv
error = 1.0
count = 1
print("n= 0 x=", a,"f(x)=",function,"f'(x)=",derv)
function = f(x)
derv = derf(x)
print("n= 1 x=", x,"f(x)=",function,"f'(x)=",derv)
while (error > epsilon):
	count = count+1
	temp = x
	function = f(x)
	derv = derf(x)
	x = x - function/derv
	error = abs(temp-x)
	function = f(x)
	derv = derf(x)
	print("n=",count,"x=",x,"error=",error,"f(x)=",function,"f'(x)=",derv)
	if(count==1000):
		break

