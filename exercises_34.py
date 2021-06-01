"""6. List sort
Create a class: Some people are standing in a row in a park. There are trees 
between them which cannot be moved. Your task is to rearrange the people by 
their heights in a non-descending order without moving the trees. People can be 
very tall!
Example
 For a = [-1, 150, 190, 170, -1, -1, 160, 180], the output should be
 sortByHeight(a) = [-1, 150, 160, 170, -1, -1, 180, 190]."""

# l1 =  [-1, 150, 190, 170, -1, -1,-1, 160, 180]
# c =[]
# class Sort:
# 	def __init__(self,l1):
# 		self.l1 = l1

# 	def Sort_list(self):

# 		for i in self.l1:
# 			if i == -1:

# 				continue
# 			c.append(i)
# 			c.sort()

# 		print(c)
# 		for i in range(len(self.l1)):

# 			if self.l1[i]== -1:
# 				print(i)
# 				c.insert(i,-1)
# 		return(c)
# x = Sort(l1)
# x.Sort_list()
# print(c)



"""4. find highest word
Create a class which given a list of strings, return another list 
containing all of its longest strings.
Example 
For inputList = ["aba", "aa", "ad", "vcd", "aba"], 
the output should be
allLongestStrings(inputList) = ["aba", "vcd", "aba"]."""

# l1=  ["aba", "aa", "ad", "vcd", "aba"]
# l2 = []

# class Higest:
# 	def __init__(self,l1,l2):
# 		self.l1 = l1
# 		self.l2 =l2
# 	def Higest_word(self):

# 		max1 = len(self.l1[0])
# 		word = self.l1[0]

# 		for i in self.l1:
# 			if len(i) > max1:
# 				max1 = len(i)
# 				word = i
# 		for j in self.l1:
# 			if len(j) == max1:
# 				self.l2.append(j)
# 		return self.l2
		
# x = Higest(l1,l2)
# x.Higest_word()
# print(l2)


"""4. find highest word
Create a class which given a list of strings, return another list 
containing all of its longest strings.
Example 
For inputList = ["aba", "aa", "ad", "vcd", "aba"], 
the output should be
allLongestStrings(inputList) = ["aba", "vcd", "aba"]."""

# n= "1254041"
# s1 =0
# s2 =0
# len1 = len(n)
# class Lucky:

# 	def __init__(self,n,s1,s2):
# 		self.n = n
# 		self.s1 = s1
# 		self.s2 = s2
# 	def Half(self):

# 		self.s1 = 0
# 		self.s2 = 0

# 		for i in self.n[0:len1//2]:
# 			self.s1+= int(i)
# 		print("First half: ",self.s1)
# 		for  j in self.n[len1//2:len1]:
# 			self.s2 += int(j)
# 		print("Second half: ",self.s2)

# 		if self.s1 == self.s2:
# 			return True

# 		else:
# 			return False
# x = Lucky(n,s1,s2)
# print(x.Half())
	
"""7. Weight
Several people are standing in a row and need to be divided into two teams. The 
first person goes into team 1, the second goes into team 2, the third goes into 
team 1 again, the fourth into team 2, and so on.You are given an array of positive 
integers - the weights of the people. Return an array of two integers, where the 
first element is the total weight of team 1, and the second element is the total 
weight of team 2 after the division is complete.
Example For a = [50, 60, 60, 45, 70], the output should be
alternating Sums(a) = [180, 105]."""

x =[]
list1 = [50,60,60,45,70,50]
s1 = 0
s2 = 0
class Weight:
	def __init__(self,list1,x,s1,s2):
		self.list1 = list1
		self.x = x
		self.s1 = list1
		self.s2 = s2
	def Weight_sort(self):
		self.s1 = 0
		self.s2 = 0
		for i in range(0,len(self.list1),2):

			self.s1 += self.list1[i]
			
		#print(s1)
		self.x.append(self.s1)
		for i in range(1,len(self.list1),2):
			self.s2 += self.list1[i]
		self.x.append(self.s2)
	
		#return self.s2
		return self.x

z = Weight(list1,x,s1,s2)
print(z.Weight_sort())
	



