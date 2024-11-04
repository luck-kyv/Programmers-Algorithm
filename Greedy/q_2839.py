N = int(input())

cnt = 0


# -3 하고 5의 배수인지 확인
while N >= 0 :
    if N % 5 == 0 :
        cnt += N // 5
        print(cnt)
        break
    N -= 3 
    cnt += 1
else:
    print(-1)