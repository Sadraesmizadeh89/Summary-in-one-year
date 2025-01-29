def l(high, Big_rule, small_rule):
    sum_rules = Big_rule + small_rule

    f = (sum_rules * high) / 2

    print(f)

high = int(input('Enter the number for high :'))

Big_rule = int(input('Enter the number for big rule :'))

small_rule = int(input('Enter the number for small rule :'))

l(high, Big_rule, small_rule)