
x =[1,2,3]

print(type(x))
#print(dir(x))
print(getattr(x,'append'))
print(hasattr(x,'append'))
print(callable(x.append))

print(id(x))