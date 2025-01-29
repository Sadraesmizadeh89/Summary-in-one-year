counter = 0

for i in range(3):
    for j in range(6):
        for t in range(11):
            for v in range(21):
                sum = i * 500 + j * 200 + t * 100 + v * 50
                if sum == 1000 :
                    counter += 1

print(f'We have {counter} mood')