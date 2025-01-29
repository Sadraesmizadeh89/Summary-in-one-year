u =int(input('enter a number :'))

for i in range(1,u):
    for j in range(1,u):
        if i == 1 or i == (u-1) or j == 1 or j == (u-1) or i == j:
            print('*' , end= ' ')
        else:
            print(' ' , end= ' ')
    print()