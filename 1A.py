import math
n, m, a = map(int, input().split())
if 1 <= n <= 1000000000 and 1 <= m <= 1000000000 and 1 <= a <= 1000000000:
    length = math.ceil(n/a)
    width = math.ceil(m/a)
    print(length*width)