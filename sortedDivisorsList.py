def divisors(integer):
    '''inputs an integer greater than 1
    returns a list of all of the integer's divisor's from smallest to largest
    if integer is a prime number returns '()is prime' '''

    divs = []
    
    if integer == 2:
        print(integer,'is prime')
                   
    else: 
        for num in range(2,integer):
            if integer%num == 0:
                divs.append(num)            
#        print(sorted(divs))
        if len(divs) == 0:
            print(integer, 'is prime')
        else:
            
            return sorted(divs)
            
        
        
            
