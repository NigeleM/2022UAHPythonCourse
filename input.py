# default type for input is a string
# input can use a prompt such as Enter a name : 
name = input("Enter a name : ")
print(name)

# must use int() to cast string input to whole number variable
number = int(input("Enter a number : "))
print(number)
# must use floatt() to cast string input to floating point number variable
floatnumber = float(input("Enter a float number : "))
print(floatnumber)

# casting types 
stringNumber = "5"
# cast string to integer
newNum = int(stringNumber)
# cast int to string
strNum = str(newNum)
# type function is used to show us the different data types

print(newNum,type(newNum),stringNumber,type(stringNumber),
     strNum,type(strNum))
     
