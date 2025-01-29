import math

def sq_xy(x_1, y_2):
    poy = ((y_1) - (y_2)) ** 2
    pox = ((x_1) - (x_2)) ** 2
    p_xy = math.sqrt(poy + pox)
    print(p_xy)
 
x_1 = int(input('Enter the number for x1 :'))

x_2 = int(input('Enter the number for x2 :'))

y_1 = int(input('Enter the number for y1 :'))

y_2 = int(input('Enter the number for y2 :'))

sq_xy(x_1, y_1)