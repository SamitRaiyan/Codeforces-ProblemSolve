word = input()
if word.isalpha():
    if len(word) <= 10:
        print(word)
    else:
        print(word[0],len(word)-2,word[len(word)-1],sep="")

        # rejected 1st time