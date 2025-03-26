n = int(input())

if not (1 <= n <= 1000):
    exit()

count = 0  

for _ in range(n):
    petya, vasya, tonya = map(int, input().split())
    
    if petya + vasya + tonya >= 2:
        count += 1

print(count)
