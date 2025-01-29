while True :
    u =int(input('Enter a number :'))  #5
    for i in range(1,u): #5 
        for j in range(1,u): 
            if i == 1 or j == 1  or i == (u-1) or j == (u-1) :
                print(end= ' * ')
            else:
                print(end= '   ')
        print()