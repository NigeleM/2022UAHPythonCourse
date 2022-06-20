
# You can add conditional statements within other conditional statements
# when you do this , this called nested conditions in the case of python
# nested if else statements

a = 100

if a > 100:
  print(a, 'is greater than 100')
elif a < 100:
  print(a,'is less than 100')
else:
  if a == 100:
    a = 101
    if a == 101:
      a = 102
      if a == 102:
        a = 103
    print(a)
  else:
    print('unknown')
    
