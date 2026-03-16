# P 제외
# 3.3 이상
# (학점 x 과목평점) 합 / 학점 총합

import sys

inp = sys.stdin.readline

score_to_grade = {
    "A+" : 4.5, "A0" : 4.0, 
    "B+": 3.5, "B0": 3.0, 
    "C+": 2.5, "C0": 2.0, 
    "D+": 1.5, "D0": 1.0, 
    "F": 0.0
}

total = 0.0
credit_sum = 0.0

for _ in range(20):
    _, b, c = inp().split()
    if c == 'P':
        continue
    credit = float(b)
    total += credit * score_to_grade[c]
    credit_sum += credit

if credit_sum == 0:
    print(0.0)
else:
    print(total/credit_sum)