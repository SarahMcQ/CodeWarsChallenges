def array_diff(a, b):
    '''inputs in two lists a and b
    if elements in a are also in b removes and returns list 
    of elements that are not in both lists '''
    
    
    newList = []
    
    if a == []:
        return a
    if b == []:
        return a
    else:
        for x in a[:]:
            if x not in b:
                newList.append(x)
        return newList
            

# best practice answers:

def array1_diff(a, b):
    return [x for x in a if x not in b]

def array2_diff(a, b):
    return [x for x in a if x not in set(b)] #set removes dupes 

def array3_diff(a, b):
    return filter(lambda i: i not in b, a)


                
    
    

