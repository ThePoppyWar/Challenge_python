

def check_palindrome_word(word):
    word = word.lower()
    if word == word[::-1]:
        return True
    else:
        return False

print(check_palindrome_word("ADA"))
print(check_palindrome_word("Kasia"))
print(check_palindrome_word("Anna"))
print("================================")

def check_palindrome_sentenc(sentenc):
    sentenc = sentenc.lower().replace(" ", "")
    if sentenc == sentenc[::-1]:
        return True
    else:
        return False

print(check_palindrome_sentenc("As I pee sir I see Pisa"))
print(check_palindrome_sentenc("I'm not a palindrome"))
