from functools import reduce


l1 = [1,2,3,4,5]
def multiply(x):
    return x*2==0
print(list(map(multiply,l1)))

l1=[1,2,3,4,5]
def multiply(x,y):
    return x+y
result =reduce(multiply,l1)
print(result)

try:
    num1 = int(input('enter the 1st value'))
    num2 = int(input('enter the 2nd value'))
    sum = num1/num2
    
except ZeroDivisionError as e:
    print(e)
    print('enter the another denominator')
else:
    print(sum)
finally:
    print('anything work here')

fruits = ["apple","banana","grape","orange"]
newlist= []
for fruit in fruits:
    if 'n' in fruit:
        newlist.append(fruits)
print(newlist)
