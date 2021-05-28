# list1 = [1,25,65,40,2]

# class Action:
# 	def __init__(self,list1):

# 		self.c = list1

# 	def max(self):

# 		list1.sort()
		
# 		print("The maximum element is: ",list1[-1])
# 	def min(self):
# 		list1.sort()
# 		print("The minimum element is: ",list1[0])
# 	def sum(self):

# 		sum1 = list1[-1] + list1[0]
# 		print(sum1)

				
# x = Action(list1)
# x.max()
# x.min()
# x.sum()


# d2 = {}
# dict1 = {"Aram":20,"Anna":25,"Van":10,"vartush":58,"valod":100}

# class Higher:

# 	def __init__(self,dict1):
# 		self.dict1 = dict1

# 	def max(self):

# 		d2 = (sorted(dict1.values()))
# 		print(d2)
# 		print("Two highest values are: ",d2[-2:])

# 		#return(list(dict1.values()[-1]))

# x= Higher(dict1)
# x.max()


# class Rectangle:

# 	def __init__(self,weight,height):

# 		self.weight = weight
# 		self.height = height
# 	def area(self):

# 		print ("area is: ", self.weight * self.height)
# x = Rectangle(10,25)
# x.area()

# class Car:

# 	def __init__(self,name,model,year,vehicle):
# 		self.name = name
# 		self.model = model
# 		self.year = year
# 		self.vehicle = vehicle

# 	def result(self):
# 		print(self.name,self.model,self.year,self.vehicle)

# class Mercedes(Car):
# 	def __init__(self,name,model,year,vehicle,qarshak,vazq):
# 		super().__init__(name,model,year,vehicle)
# 		self.qarshak = qarshak
# 		self.vazq = vazq
# 	def qar(self):
# 		return "vazq is 230000 km,vehicle is 2.5"

# class Bmw(Car):
# 	def __init__(self,name,model,year,vehicle,guyn,tapq):

# 		super().__init__(name,model,year,vehicle)
# 		self.guyn = guyn
# 		self.tapq = tapq
# 	def guyn1(self):
# 		return "guyn is black" ,"tapq is sedan"

# x= Mercedes("mers","s222","2020","3.0","4x4",20000)
# print(x.qar())
# x.result()
# y = Bmw("bmw","f20",2019,3.5,"black","sedan")
# print(y.guyn1())
# y.result()

class Armenia:
	def city(self):
		print("Yerevan")
class France:
	def city(self):
		print("Paris")
a=Armenia()
b=France()

a.city()
b.city()