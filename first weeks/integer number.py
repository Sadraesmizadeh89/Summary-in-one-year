integer = 12345

dah_hezargan = integer // 10000
#print(dah_hezargan)
hezargan = integer // 1000
m_hezargan = hezargan % 10
#print(m_hezargan)
sadgan = integer // 100
m_sadgan = sadgan % 10
#print(m_sadgan)
dahgan = integer // 10
m_dahgan = dahgan % 10
print(m_dahgan)
yekan = integer // 1
m_yekan = yekan % 10
#print(yekan)
s1 = str(dah_hezargan) + '   '
s2 = str(m_hezargan) + '   '
s3 = str(m_sadgan) + '   '
s4 = str(m_dahgan)  + '   '
s5 = str(m_yekan) + '   '

print(s1, s2, s3, s4, s5)