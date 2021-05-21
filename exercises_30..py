# def bin(n):

# 	if n >1:
# 		bin(n//2)

# 	print(n%2, end ="")
# bin(8)

""" Function
Given three numbers a, b (a ≤ b) and step. Create an list of 
evenly spaced elements starting from a to b spaced by 
step. you have 3 argument:"""

# list2 = []
# x= int(input("enter the x: "))
# y= int(input("enter the y: "))
# z= int(input("enter the z: "))	
# def list1(x,y,z):

# 	for i in range(x,y+1,z):
# 		list2.append(i)
# 	return(list2)
# print(list1(x,y,z))


"""2. List
Write a function. Create the list which elements are 
products between two neighbours.
Input Output"""

# l3 = []
# list2 = [3, 7, 12, 5, 20, 0]
# def l1(list2):

# 	for i in range(len(list2)):

# 		x= [list2[i]*list2[i+1] for i in range(len(list2)-1)] 
# 	l3.append(x)
# 	return l3

# print(l1(list2))



"""3. New sentence
Given a sentence with missing words and an array of 
words. Replace all ‘_’ in a sentence with the words from the 
array"""

# str1 = "_, we have a _.".split(" ")
# list1 = ["Ashot","problem"]
# c= 0
# for i in range(len(str1)):
# 	if i == "_":
# 		str1[i] = list1[c]
# 		c+=1
# print(list1.join(str1))


"""4. sum word
Given a list of strings. Find the strings with maximum and 
minimum lengths in array. Print the sum of their lengths.
Input: [“anymore”, “raven”, “me”, “communicate”] 
Output: 13"""

# sum = 0
# list1 = ["anymore", "raven", "me", "communicate"]

# list1.sort(key = len)
# print(list1)

# sum = len(list1[0]) + len(list1[-1])
# print(sum)


"""5. find index
Given a list of numbers and a number. Find the index of a 
first element which is equal to that number. If there is not 
such a number, that find the index of the first element 
which is the closest to it"""

# n= int(input("enter the number: "))
# list1 = [21, -9, 15, 2116, -71, 33]
# l2 = []

# for i in range(len(list1)):

# 	if n in list1:

# 		print(n,i)
# 		break
# 	else:

# 	 	a =abs(n-list1[i])
# 	 	l2.append(a)
# 	 	print(l2.index(min(l2)))
# 	 	break

"""6. New Dict
Define a function which can generate a dictionary where 
the keys are numbers between 1 and N (both included) and 
the values are square of keys. The function should print the 
dict.Example : 
N = 5 
{1: 1, 2:4, 3:9, 4:16, 5:25}"""


# n= int(input("enter the number: "))

# d = dict()
# def dict1(n):


# 	for i in range(1,n+1):

# 		d[i] = i**2
# 	return(d)
# print(dict1(n))

		
""" Given an dict. Invert it (keys become values and values 
become keys). If there is more than key for that given value 
create an list.Input 
{ a: ‘1’, b: ‘2’, c: ‘2’ }
Output 
{ 1: ‘a’, 2: [‘b’, ‘c’] } """

# dict1 = { "a": "1", "b": "2", "c": "2"}
# dict2 = {}

# for key,value in dict1.items():

# 	if value in dict2:
# 		dict2[value].append(key)
# 	else:
# 		dict2[value] = [key]
# for i in dict2:
# 	print(dict2)
# 	break



"""8. FIBONACCI
Write a function using recursion to find fibonacci numbers:"""

# n = int(input("enter the number: "))
# def rec_fib(n):
# 	if n <=1:
# 		return n
# 	else:
# 		return rec_fib(n-1)+rec_fib(n-2)

# x= 10

# if n<= 0:
# 	print("only positive number: ")
# else: 
# 	for i in range(x):
# 		print(rec_fib(i))
