text = input("Enter a sentence: ")
words = text.split()
frequency = {}
for word in words:
    word = word.lower()
    if word in frequency:
        frequency[word] += 1
    else:
        frequency[word] = 1
for word, count in frequency.items():
    print(word, count)


