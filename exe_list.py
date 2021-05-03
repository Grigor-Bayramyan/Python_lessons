#list = [6,"hi",12.15,(45,5),[7,8],True]
# c= "!@#$%^&*))"
# while True:
# 	number_c= 0
# 	char_c = 0 
# 	password = input("enter your pass:")


# 	if len(password) <8:
# 		print("your password must be great than 8")
# 		continue
# 	if not password[0].isupper():
# 		print("your password must be upper")
# 		continue
# 	for i in password:
# 		if i.isdigit():
# 			number_c+=1
# 		elif i in c:
# 			char_c+=1
# 	if number_c <2 and char_c <2:
# 		print("your password must be have two numbers and char")
# 		continue
# 	print("strong")
#	break




# link = "https://www.youtube.com/watch?v=IGN9cIwXH0A"
# print(link[link.index("=")+1:])
# user = input("enter the word:")

# if user == user[::-1]:
# 	print("ok")
# else:
# 	print("bad")

 # list1 = [1,2,2,3,3,3,3,"hi","p","hi"]
# c= 0
# for i in range(len(list1)):

# 	if list1.count(list1[c]) >1:
# 		list1.remove(list1[c])
# 		c -=1
# 	c+=1
# print(list1)
# list2 =[]
# for i in  list1:
# 	if i not in list2:


# 		list2.append(i)
# print(list2)

# list1 = [1,2,2,3,45,6]
# c=0
# list2 =[]
# for i in range(len(list1)):
# 	if list1[c] %2 == 0:
# 		del list1[c]
# 		c -=1
# 	c+=1
# print(list1)

list1 = [4,2,5,"dhdj"]
res =[]
for i in list1:
	if i in list1 and i %2 ==0:
		res.append(i)
print(res)
