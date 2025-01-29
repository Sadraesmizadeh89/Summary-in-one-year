quiz1 =float(input('Please enter your first quiz score :'))

quiz2 =float(input('Please enter your second quiz score :'))

midterm_exam =float(input('Please enter your midterm exam score :'))

final_exam =float(input('Please enter your final exam score :'))

q = (quiz1 + quiz2) *(25 / 100)

m = midterm_exam *(25 / 100)

f = final_exam *(50 / 100)

Total_scores = q + m + f

last_stage = Total_scores * 5

if 90 <= last_stage <= 100 :
    print('A')
elif 80 <= last_stage < 90 :
    print('B')
elif 70 <= last_stage < 80 :
    print('C')
elif 60 <=last_stage < 70 :
    print('D')
elif 0 <= last_stage < 60  :
    print('E')
else:
    print('please try again')