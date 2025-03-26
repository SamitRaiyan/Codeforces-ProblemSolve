M, N = map(int, input().split())

if 1 <= M <= N <= 16:
    max_dominoes = (M * N) // 2
    print(max_dominoes)