from functools import reduce

listx=[1,2,3,4,5,6,7,8]
r=reduce(lambda x,y:x+y,listx)
print(r)


listy = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
t = reduce(lambda x, y: x+y, listy,'ssss')
print(t)
