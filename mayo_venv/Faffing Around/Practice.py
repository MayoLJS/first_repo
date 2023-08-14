items = ['bread','beans','biscuit']
items[0]
items[0]='chips'
print(items)
items = ['bread','beans','biscuit']
items.append('butter')
print(items)


items = items+['sweet','dance']
items

sqs =[0,1,4,9,16,25,36,49,64]
print(sqs[1::4])


num = input('Enter a number: ')
num=int(num)
if num%2==0:
    print('even')
else:
    print('odd')
    

sqs=[0,1,4,9,16,25,36,49,64,81]
res = sqs[::-1]
print(res[2])

# find last character
text = input('Type your sentence')
rev = text[::-1]
print(rev[0])

# Dish checker
indian=['samosa','daal','naan']
chinese=['egg roll','pot sticker','fried rice']
italian=['pizza','pasta','risotto']

dish = input ('Enter a dish name: ')

if dish in indian:
    print('indian')
elif dish in chinese:
    print('chinese')
elif dish in italian:
    print('italian')
else:
    print('i no sabi abeg this',dish)
    
# Loop
exp = [20, 40, 50, 60, 70, 80, 90, 70, 20, 55, 66]
total = 0
for item in exp:
    total = total + item
print(total)

# FUNCTIONS
##First you prepare the function
def calculate_total (exp):  #Function Argument
    total = 0                                       #Whole thing is FUNCTION BODY
    for item in exp:
        total=total+item
    return total            #Function Return Value

##This is what you want to add together
mayowa_expense = [1500, 2000, 5000]
onotie_expense = [5000, 8000, 1500]

##Calling the "calculate total" function here
mayowa_total_expense = calculate_total(mayowa_expense)
onotie_total_expense = calculate_total(onotie_expense)

print ("Mayowa's total expense is: ",mayowa_total_expense)
print ("Onotie's total expense is: ",onotie_total_expense)


# Another example
def sum(a,b):
    """
    This is documentation
    """
    total=a+b
    return total
n = sum(6,7)
print ('Total is ', n)

import math
dir(math)
math.asinh(5)

import calendar
calendar.month(2022,8)

list = [1, 1, 2, 3, 5, 8, 13]
print(list[list[4]])

for i in range(10):

  if not i % 2 == 0:

    print(i+1)
    
    
x = [6, 4, 2, 9]

x = x[::-1]

print(x[0]+x[2])


N = int(input())

# Calculating the sum of numbers from 1 to N
sum_of_numbers = (N * (N + 1)) // 2

print(sum_of_numbers)