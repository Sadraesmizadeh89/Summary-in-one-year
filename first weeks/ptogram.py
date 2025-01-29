a =int(input('Enter a 4 digit number :'))

s = a // 1000

g = a // 100
c = g % 10

u = a // 10
o = u % 10

e = a % 10


print(f'{e}    {o}    {c}    {s}')
