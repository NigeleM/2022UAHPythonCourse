# def show(s):
#   print(s)

# show('nigele mccoy')
# show('apple')

# def add(x,y):
#   return x+y

# for num in range(0,15):
#   print(add(num,num+9))
  

# def sumoflist():
#   count = 0
#   numbers =[1,2,3,4]
#   for num in numbers:
#     count += num
#   return count

# print(sumoflist())

# def displaylist():
#   names = ['vivi','nancy','xa-quan','nigele']
#   for name in names:
#     print(name)

# displaylist()


# Recursive Python function to solve the tower of hanoi
 
# def TowerOfHanoi(n , source, destination, auxiliary):
#     if n==1:
#         print ("Move disk 1 from source",source,"to destination",destination)
#         return
#     TowerOfHanoi(n-1, source, auxiliary, destination)
#     print ("Move disk",n,"from source",source,"to destination",destination)
#     TowerOfHanoi(n-1, auxiliary, destination, source)
         
# # Driver code
# n = 4
# TowerOfHanoi(n,'A','B','C')
# # A, C, B are the name of rods
 
# # Contributed By Dilip Jain



# def binarySearch(arr, l, r, x):
 
#     # Check base case
#     if r >= l:
 
#         mid = l + (r - l) // 2
 
#         # If element is present at the middle itself
#         if arr[mid] == x:
#             return mid
 
#         # If element is smaller than mid, then it
#         # can only be present in left subarray
#         elif arr[mid] > x:
#             return binarySearch(arr, l, mid-1, x)
 
#         # Else the element can only be present
#         # in right subarray
#         else:
#             return binarySearch(arr, mid + 1, r, x)
 
#     else:
#         # Element is not present in the array
#         return -1
 
 
# Driver Code
# arr = [2, 3, 4, 10, 40]
# x = 10
 
# # Function call
# result = binarySearch(arr, 0, len(arr)-1, x)
 
# if result != -1:
#     print(f"Element {x} is present at index % d" % result)
# else:
#     print(f"Element {x} is not present in array")



#change algorithm

def change(n):
    dicts = {}
    total = n
    quarter = 0
    dime = 0
    nickles = 0
    pennies = 0
    
    while total != 0:
        if total % 25 >= 0 :
            quarter = total//25
            total %= 25
            dicts['quarter'] = quarter
        if total % 10 >= 0:
            dime = total // 10
            dicts['dime'] = dime
            total %= 10
        if total % 5 >= 0:
            nickles = total // 5
            dicts['nickles'] = nickles
            total %= 5
        if total % 1 >= 0:
            pennies = total // 1
            dicts['pennies'] = pennies
            total %= 1
            #print(total)
        #print(dicts)

    return dicts
print(change(999))
print(change(0))
print(change(205))
print(change(2529))


# import random

# def lotto():
#     numbers = set()
#     rangeWhite = 70
#     rangeRed = 25
#     count = 0
#     while len(numbers) != 5:
#         white = random.randrange(1,rangeWhite)
#         numbers.add(white)
#         rangeWhite -= 1


#     while len(numbers) != 6:
#         red = random.randrange(1,rangeRed)
#         numbers.add(red)
#         rangeRed -= 1
#         power = red
#     return numbers, power

# lotto()

# print(lotto())
# print(lotto())
# print(lotto())
# print(lotto())
# print(lotto())
# print(lotto())
# print(lotto())

"""Good morning! Here's your coding interview problem for today.
This problem was asked by Microsoft.
Given an array of numbers and a number k, determine if there are three entries
in the array which add up to the specified number k. For example,
given [20, 303, 3, 4, 25] and k = 49, return true as 20 + 4 + 25 = 49."""

# my solution is to use a permutations
# import itertools
# def main(n,k):
#     List=list(itertools.permutations(n, 3))
#     for solution in List:
#         if k == sum(solution):
#             return True

#     return False
            
# print(main([20, 303, 3, 4, 25],49))
# print(main([20, 303, 3, 4, 25],310))
# print(main([100, 100, 3, 4, 25],203))
# print(main([100, 100, 3, 4, 25],53))
# print(main([20, 303, 3, 4, 25],99))


# Implement autocomplete system
# Implement an autocomplete system. That is, given a query strings and a set of all
# possible query strings, return all strings in the set that haves as a prefix.
# For example, given the query string de and the set of strings [dog, deer, deal]:
# return [deer, deal].

# WORDS = ['dog','deer','deal']
# def autocomplete(s):
#   results = set()
#   for word in WORDS:
#     if word.startswith(s):
#       results.add(word)
#   return results

# print(autocomplete('de'))

