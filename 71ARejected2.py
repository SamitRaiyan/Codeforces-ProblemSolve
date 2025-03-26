n = int(input())

if 1 <= n <= 100:
    words = input().split()

    if len(words) == n:
        for word in words:
            if not word.isalpha() or not word.islower():
                break
            elif not (1 <= len(word) <= 100):
                break
            else:
                if len(word) > 10:
                    print(word[0] + str(len(word) - 2) + word[-1])
                else:
                    print(word)


# rejected 2nd time