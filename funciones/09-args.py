

def big_function(*args,**kwargs):    
    total = 0
    for item in kwargs.values():
        total+= item
    return total + sum(args)        
        
    
    

print(big_function(1,1,1,1,1,1,1,1,1,num=1,num2=1))    