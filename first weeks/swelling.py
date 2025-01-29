def swelling(p_p_y, p_t_y):
    swelling = (p_t_y - p_p_y) / p_p_y
    h_s = swelling / 100
    print(h_s)
    print(f'The next year is price according to the inflation rate is equal to: {(p_p_y + p_t_y) * swelling}')


p_p_y = int(input('What was the price of this product last year?'))

p_t_y = int(input('What was the price of this product this year?'))

swelling(p_p_y, p_t_y)