"""fruits = ["apple","banana","grape","orange"]


result = [fruit for fruit in fruits if 'n' in fruit]
print(result)"""

"""list = [1,2,3,4]
n=2
new_list = [i*n for i in list]
print(new_list)"""

keys = ['a','b','c','d']
values = [1,2,3,4]
a = zip(keys,values)
print(list(a))


dict_values = {k:v for (k,v) in zip(keys,values) }
print(dict_values)