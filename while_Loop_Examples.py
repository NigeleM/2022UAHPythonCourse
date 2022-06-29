
status = True
while status:
  
  print("*** \tSelect operation.\t ***")
  print("*** \t1.Add\t\t\t\t ***")
  print("*** \t2.Subtract\t\t\t ***")
  print("*** \t3.Multiply\t\t\t ***")
  print("*** \t4.Divide\t\t\t ***")
  choice = input("Enter choice(1/2/3/4): ")
  if choice in ('1', '2', '3', '4'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        if choice == '1':
          print(num1, '+', num2, "=", num1+num2)
      
        elif choice == '2':
          print(num1, "-", num2, "=", num1-num2)
      
        elif choice == '3':
          print(num1, "*", num2, "=", num1*num2)
      
        elif choice == '4':
          print(num1, "/", num2, "=", num1/num2)

  option = input("Enter y to calculate again or n to exit : ")
  if option == 'y':
    print()
  else:
    status = False
