"""1.Create 5 file (.txt) and write messages in 
them."""

# file_name = "exercises.txt"
# def f1(file_name):
# 	try:
# 		file = open(file_name,"w")

# 		file.write("hi i'm here")
# 	except FileNotFoundError:

# 		return "there are not this file"
# 	finally:
# 		file.close()
# print(f1(file_name))

"""2. Write a Python program to read first n lines of
a file."""

# n= int(input("enter the n: "))
# def read_lines(file_name,n,mode = "r"):

# 	with open(file_name) as f:
# 		for lines in range(n):

# 			print(f.readline())
# read_lines("exercises.txt",n)


"""3.Write a Python program to append text to a file and
display the text."""

# file_name = "exercises.txt"
# def f1(file_name):
# 	try:
# 		file = open(file_name,"a")

# 		file.write("\nhello world")
# 	except FileNotFoundError:

# 		return "there are not this file"
# 	finally:
# 		file.close()
# print(f1(file_name))

"""4.Write a python program to find the longest words"""

# def long_word(file_name,mode ="r"):

# 	with open(file_name) as f:
# 		f1 = f.read().split()

# 		l1 = ""
# 		for i in f1:
# 			if len(i) > len(l1):

# 				l1 = i
			
# 		print(l1)
# long_word("exercises.txt")

"""//////////////////////////////"""
# 		words = list(f.read().split())

# 		words1= sorted(words)
# 		print(words)
# 		print(words[-1])
# long_word("exercises.txt")

"""5.Write a python program to find numbers in txt."""
# def find_num(file_name):

# 	with open(file_name,"r") as f:
		
# 		for line in f:
# 			#words = line.split()

# 			for i in f:

# 				for number in i:


# 					if number.isdigit():

# 						print(number)
# (find_num("exercises.txt"))

"""6.Write a python program to get login and password"""

# def log_pas(file_name):
# 	with open(file_name,"w") as f:

# 		password = input("your password ")
# 		login = input("your login ")
# 		res = f"password is {password}\nLogin is {login}"
# 		f.write(res)
# 	print(f.closed)
# (log_pas("exercises.txt"))