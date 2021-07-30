import math
for _ in range(int(input())):
    for _ in range(int(input())):
        I,N,Q = map(int,input().split())
        if (N % 2 == 0 or I == Q):
            print(math.floor(N/2))
        else:
            print(math.floor(N/2 + 1))
    