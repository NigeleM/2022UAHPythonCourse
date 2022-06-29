
# file = open('accounts.txt','r')
# for line in file:
#   info = line.split(',')
#   if info[0] == 'Account Owner':
#     continue
#   else:
#     info[2] = info[2].replace('\n','')
#     print(f'{info[0]} has {info[1]} in their checking and {info[2]} in their savings account')
# file.close()

sumInBank = 0
file = open('accounts.txt','r')
for line in file:
  info = line.split(',')
  if info[0] == 'Account Owner':
    continue
  else:
    sumInBank += int(info[2])
file.close()

print(f'The total amount the bank is holding is in saving is {sumInBank}')
