def is_vowel(letter):
    return letter in ['a', 'e', 'i', 'o', 'u', 'y']

def score_words(words):
    score = 0
    for w in words:
        count = 0
        for l in w:
            if is_vowel(l):
                count += 1
        if count % 2 == 0:
            score += 2
        else:
            score += 1#there's not a operator ++ in python
    return score

n = int(input())
words = input().split()
print(score_words(words))
