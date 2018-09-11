def tickets(people):
    ''' input a list of people purchasing $25 movie tickets 
    returns wether or not clerk can return change if start clerk
    starts with with $0'''
    
    change = 0
    
    for x in people:
        if x == 25:
            change += x
        if x == 50:
            change -= 25
        if x == 100:
            change -= 75
    if change < 0:
        print("NO. .Vasya will not have enough money to give change to",people[-1],"dollars")
    if change >= 0:
        print("YES")