"""Factorial

1. Create a python function
factorial and import this 
file in another file and 
print factorial."""

# def fact(n):

# 	if n == 0:
# 		return 1
# 	elif n >0:

# 		for i in range(1,n+1):
# 			res = n*fact(n-1)
# 		return res
# n = int(input("enter the number: "))

"""Cylinder

2.Write a Python function to 
calculate surface volume and area of 
a cylinder(Գլան).
V=πr^2h and A=2πrh+2πr^2 :"""

# import math
# r= int(input("enter the r: "))
# h= int(input("enter the h:"))
# def cylinder(r,h):

# 	try:
# 		if r and h == 0:

# 			raise Extention("your h and r must be greater than 0")
# 	except Extention as r:
# 		print(r)

# 	V = 2*math.pi*r
	
# 	S= 2*math.pi*r*h

# 	return V,S

"""Surface

3. Write a Python function 
to calculate surface volume 
and area of a sphere(Գունդ).
V = 4/3*π*r3 and A = 4*π*r2"""


# import math
# r= int(input("enter the r: "))

# def surface(r):

# 	try:

# 		if r == 0:
# 			raise Extention("your r doesn't must be 0 ")
# 	except Extention as r:

# 		print(r)

# 	V= 4/3 * math.pi*pow(r,3)

# 	A = 4*math.pi*pow(r,2)

# 	return V,A


"""4. Write a Python function 
to convert degree to radian.
one radian = pi/180:
90 radian = 1.57..."""

# import math
# rad = 0
# deg = int(input("enter the degree: "))

# def deg_rad(deg):

# 	if deg == 0:

# 		return rad
# 	else:

# 		rad = deg* 180/math.pi

# 		return rad


"""5. Write a Python function to print 
all primes smaller than or equal to a 
specified number.
Call function:numbers(9)
Output: (2, 3, 5, 7) """

# import math
# n = int(input("enter the your favorite number: "))

# def prime_num(n):


# 	try:

# 		if n ==0:

# 			raise Extention("you can not input 0 ")
# 	except Extention as r:

# 		print(r)
# 	for n in range(1,n+1):

# 		if n >1:

# 			for i in range(2,n):
# 				if n % i == 0:

# 					break

# 			else:

# 				print(n)

				


