#title: word separator
#author: michael stoll
#date: 3/17/2025
result = ' '
squished_words = str(input('Enter sentence without spaces and where each word is capitalized:'))
result = result + squished_words[0]
for c in range(1, len(squished_words)):
    character = squished_words[c]
    if character.isupper():
        character = character.lower()
        result = result + ' '
    result = result + character
print(result)