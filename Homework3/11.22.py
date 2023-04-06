# George Tannous 1971969
# 11.22
Words = input("")
ListOfWords = Words.split()

wordsFreq = {}

for i in range(0, len(ListOfWords)):
    word = ListOfWords[i]
    if word not in wordsFreq:
        wordsFreq[word] = 1
    else:
        wordsFreq[word] = wordsFreq[word] + 1

for i in range(0, len(ListOfWords)):
    print(ListOfWords[i], wordsFreq[ListOfWords[i]])
