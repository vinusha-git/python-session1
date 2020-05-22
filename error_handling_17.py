#divide by zero
x=2
y=0
try:
    print(x/y)
except ZeroDivisionError as e:
    print('not allowed to divide')
else:
    print('something went wrong')
finally:
    print('this is our clean up code')
