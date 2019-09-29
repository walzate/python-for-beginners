# String operations
sentence = 'This is a common sentence'

print(sentence.upper())
print(sentence.lower())
print(sentence.capitalize())
# Counting the number of times of letter m in the sentence
print(sentence.count('m'))

# Getting information from the console now with format function
first_name = input ('What is your name? \n')
last_name = input ('What is your last name? \n')
text = 'Hello {0} {1} nice to meet you!'.format(first_name.capitalize(), last_name.capitalize())
print(text)
# Only in Python 3
text = f'Hello {first_name} {last_name} in Python 3'
print (text)