def shorten(sentence):
    sentence_1 = sentence.upper().split()
    result = ""
    for word in sentence_1:
        result += word[0]
    return result


shortened = shorten("Don't repeat yourself")
print(shortened)
shortened = shorten("Read the fine manual")
print(shortened)
shortened = shorten("All terrain armoured transport")
print(shortened)
