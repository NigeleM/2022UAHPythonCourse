# Lists are used to store multiple items in a single variable.

# Lists are one of 4 built-in data types in Python used to store collections of data, the other 3 are Tuple, Set, and Dictionary, all with different qualities and usage.

# Lists are created using square brackets

empty = []
names = ['Joe','Jasmine','Mark','Nicole']
numbers = [1,2,3,4] 


# print(numbers)
# print(names)

# # len function
# print(len(numbers))
# print(len(names))

# # list()
# letterlist = list('abcd')
# print(letterlist)
# newNumbers = list((1,2,3,4,5)) 
# print(newNumbers)
#print(dir(list()))
# newName = input("Enter a name : ")
# # append function
# names.append(newName)
# print(names)
# remove function
# delName = input("Enter a name you want to delete: ")
# names.remove(delName)
# print(names)
#insert function
# insertName = input("Enter a name you want to insert: ")
# names.insert(0,insertName)
# print(names)    `
# list comprehension
# num = [x for x in range(10)]
# print(num)
#get certain index
# print(names[0])
# print(names[3])

#sorted function
# names = sorted(names)
# print(names)


# Dictionary items are ordered, changeable, and does not allow duplicates.

# Dictionary items are presented in key:value pairs, and can be referred to by using the key name.

# passwordDict = {'nigele':'123password','Quan' : [1,'info']}
# print(passwordDict)
# # Get functions  
# print(passwordDict['nigele'])
# print(passwordDict.get('nigele')) 
# print(passwordDict.get('Quan'))
# # values function
# print(passwordDict.values())
# # keys function
# print(passwordDict.keys())

# import getpass

# password = getpass.getpass("Enter password : ")
# passwordDict['nigele'] = password
# print(passwordDict['nigele'])

#Sets are used to store multiple items in a single variable.

# Set is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Tuple, and Dictionary, all with different qualities and usage.

# A set is a collection which is unordered, unchangeable*, and unindexed.

# fruitset = {"apple", "banana", "cherry"}
# # add function
# fruitset.add("orange") 
# print(fruitset)

# fruitset = {"apple", "banana", "cherry"}
# tropical = {"pineapple", "mango", "papaya"} 
# tropical = sorted(tropical)
# # update function
# fruitset.update(tropical)
# print(fruitset)

# fruitset = {"apple", "banana", "cherry"}
# # remove function
# fruitset.remove("banana")
# print(fruitset)

# set1 = {"a", "b" , "c"}
# set2 = {1, 2, 3}
# # union
# set3 = set1.union(set2)
# print(set3)

# x = {1,2,3,4}
# y = {2,4,5}
# # intersection
# z = x.intersection(y)
# print(z)
