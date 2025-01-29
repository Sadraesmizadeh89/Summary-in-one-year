import random

n = random.randrange(0,100)

s =input('Enter(hard , miduem , easy):')

if s == 'hard' :
    g = 4
elif s == 'miduem' :
    g = 6
elif s == 'easy' :
    g = 8

while g >= 0 :
    a = int(input("Enter a number : (0 , 100) :"))
    print(f'you have {g - 1} chance')
    print()

    if a == n :
        print("its Correct!")
        g = "yes"
        break
    elif a < n :
        print("please enter large number! ")
    elif a > n :
        print("please enter smaller number! ")
    g -= 1
    if g == 0 :
        print(f'you lost . the computer choice is {n}')
        break