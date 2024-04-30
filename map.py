listx=[1,2,3,4,5,6,7,8]
listy=[2,3,4,5,6,7,8,9]
r = map(lambda x, y: x*x+y, listx, listy)
print(list(r))