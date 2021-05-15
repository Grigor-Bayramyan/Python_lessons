"""1. Dict
You have two list convert it in dictionary and add
in (mydict.txt) and show result:"""

# list1 = ["Ann","Anita","Bob","isabell"]

# list2 = [10,20,15,30]

# dict1 = {i:j for i,j in zip(list1,list2)}

# print(dict1)

"""2. Json
Create json file and save them lyrics (song)
and print in cmd word this song."""

# import json
# file_name = "exe_27.json"

# dict1 = {"anapati arev":"Karotel em, karotel emSev achere yaris karotel em Karotel em, karotel em Anush dzaynd karotel em Ax anapati champeqin qarot Ax im yare mnatsel e karot Ax yerani tev arni u ga"}

# name_song = input("enter the name_song: ")

# if name_song in dict1:
# 	print(dict1["anapati arev"])

# with open(file_name,"w") as f:

# 	json.dump(dict1,f)

"""3. Function
Write a python program which have one input an
integer, representing the sum of all the multiples of
3 and 5 below the given input. and save this result
in json file.
for example:
input 10 (3, 5, 6 and 9)
output:23"""

# import json

# file_name = "exe_27.json"
# number = int(input("enter the number: "))

# sum1 = 0
# for i in range(1,number):

# 	if i % 3 == 0 or i % 5 ==0:

# 		sum1+=i
# print(sum1)



# with open(file_name,"w") as f:

# 	json.dump(sum1,f)

""" 4. Vowels
Write a program that takes in a string as input,
counts and outputs the number of vowels.
And add result in json file.
for example:
input: test
output: 1"""

import json

file_name = "exe_27.json"

vowels = ("a","A","e","E","i","I","o","O","u","U")

word = input(("enter the word: "))

count = 0

for i in word:

	if i in word:

		count+=1
print(count)









