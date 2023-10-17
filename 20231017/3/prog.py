from string import digits
from string import punctuation
from collections import Counter

change = set(digits) | set(punctuation)

n = int(input())
words = Counter()

while (s := input()):
    s = s.lower()
    for i in s:
        if i in change:
            s = s.replace(i, ' ')

    for word in s.split():
        if len(word) == n:
            words[word] = words.setdefault(word, 0) + 1

if len(words):
    max_count = words.most_common()[0][1]
    for word, count in words.most_common():
        if count == max_count:
            print(word, end = ' ')
        else:
            break
    print()

