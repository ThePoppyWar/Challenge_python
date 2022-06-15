def palindorm(word):
    word = word.lower()
    if word == word[::-1]:
        return True
    else:
        return False

word_1 = "kajak"
word_2 = "anakonda"

print(palindorm(word_1))
print(palindorm(word_2))

# or
print("+++++++++++++++++++++++++++++++++++++")

def palindorm_2(word):
    word = word.lower()
    return True if word == word[::-1] else False

word_3 = "Anna"
word_4 = "Marchewka"

print(palindorm_2(word_3))
print(palindorm_2(word_4))
