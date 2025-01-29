def l(age):
    age_by_day = 365.25 * age

    age_by_mounth = age_by_day / 30

    age_by_second = age_by_day * 24  * 60 * 60

    print(f'your age is equal to : {age_by_day} day')

    print(f'your age is equal to : {age_by_mounth} mounth')

    print(f'your age is equal to : {age_by_second} second')


age = int(input('How old are you ?'))

l(age)