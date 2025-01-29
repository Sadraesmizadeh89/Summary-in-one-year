import random

print('paer , rock , scissor')

bot_chois =['scissor' , 'rock' , 'paper']

uc = 0

bo = 0


for u in range(6):
    uc1 =input('Enter a number for your choice :')
    bot =random.choice(bot_chois)
    if uc1 == bot :
        print(f'you are equal the computer choice is: {bot}')
        uc += 0
        bo += 0


    elif uc1 == 'scissor' :
        if bot == 'paper':
            print(f'you are won the computer choice is: {bot}')
            uc += 1
            bo += 0

    elif bot == 'rock' :
        print(f'you are lost the computer choice is : {bot}')
        uc += 0
        bo += 1


    elif uc1 == 'paper':
        if bot == 'scissor' :
            print(f'you are lost the computer choice is : {bot}')
            uc += 0
            bo +=1

        elif bot == 'rock' :
            print(f'you are won the computer choice is : {bot}')
            uc += 1
            bo += 0


    elif uc1 == 'rock':
        if bot == 'scissor' :
            print(f'you are won the computer choice is : {bot}')
        elif bot == 'paper' :
            print(f'you are lost the computer chois is : {bot}')
            uc += 0
            bo +=1
    else:
        print('Enter the appropriate amount')
if uc > bo :
    print('you won !! I hope you like this game')
elif uc == bo :
    print('you equal !! I hope you like this game')
else:
    print('you are lost !! I hope you like this game')