# K번째 약수

# 1. 입력
# 2. 약수 찾기

N, K = map(int, input().split())
flag = False

for i in range(1, N+1):
    if (N%i) == 0:
        K-=1
        if K == 0: 
            print(i)
            flag = True
            break

if flag is False: print(-1)

for i in range(1, N+1):
    if (N%i) == 0:
        K-=1
        if K == 0: 
            print(i)
            break
else:
    print(-1)