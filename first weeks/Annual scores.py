quiz1 =float(input('Please enter your first quiz score :'))

quiz2 =float(input('Please enter your second quiz score :'))

midterm_exam =float(input('Please enter your midterm exam score :'))

final_exam =float(input('Please enter your final exam score :'))

q = quiz1 + quiz2 * 5

qm = q * (25/100)

sum_m_qm = qm + ((25 / 100) * midterm_exam)

final_stage = sum_m_qm + ((50 / 100) * final_exam)

print(f'Your average score during the semester was {final_stage}')