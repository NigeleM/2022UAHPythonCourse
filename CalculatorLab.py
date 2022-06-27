# Create a calculator 
# must be able to "+ / - * ** %1 
num1 = float(input("Enter a number : "))
num2 = float(input("Enter a number 2 : "))
operand = input("enter operator + / - * ** % :")
if operand == "+":
  total = num1 + num2 
  print(total)
elif operand == "-":
  total = num1 - num2 
  print(total)
elif operand == "/" and num2 == 0:
  print("Cant divide by zero")
elif operand == "/":
    total = num1 / num2 
    print(total)
elif operand == "*":
  total = num1 * num2 
  print(total)
elif operand == "**":
  total = num1 ** num2 
  print(total)
elif operand == "%":
  total = num1 % num2 
  print(total)
 
