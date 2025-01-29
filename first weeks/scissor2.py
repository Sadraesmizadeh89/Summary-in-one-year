c1 = 0

c2 = 0

for k in range(6):
    player1 =int(input('Enter a number for player1 1:(sc) , 2:(ro) , 3:(pa)'))
    print()
    player2 =int(input('Enter a number for player2 1:(sc) , 2:(ro) , 3:(pa)'))

    if (player1 == 1 and player2 == 3) or (player1 == 2 and player2 == 1) or (player1 == 3 and player2 == 2) :
        c1 += 1
    elif (player2 == 1 and player1 == 3) or (player2 == 2 and player1 == 1) or (player2 == 3 and player1 == 2):
        c2 += 1
    else:
        continue
if c1 > c2 :
    print(f'player1 won player1 point is {c1}')
elif c1 < c2:
    print(f'player2 won player2 point is {c2}')
else:
    print(f'you are equal the player1 point is {c1} and player2 point is {c2}')