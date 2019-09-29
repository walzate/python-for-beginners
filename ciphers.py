def reverse_text(input_text):
    reversed_text = input_text[::-1]
    return reversed_text

def text_to_list(text):
    return list(text)

def atbash(text):
    alphabet = 'abcdefghijklmnñopqrstuvwxyz'
    reversed_alphabet = reverse_text(alphabet.upper())
    reversed_alphabet_list = text_to_list(reversed_alphabet)
    text_list = text_to_list(text.lower())
    text_cyphered = ''
    for character in text_list:
        index = alphabet.find(character)
        if index >= 0 :
            text_cyphered = text_cyphered + reversed_alphabet_list[index]
        else:
            text_cyphered = text_cyphered + character
    return text_cyphered
 
def get_next_character_in_list (character, dict):
    index = dict.find(character)
    if index >= 0 and (index + 1) <= len(dict)-1:
        result = dict[index + 1]
    elif index == len(dict)-1:
        result = dict[0]
    else:
        result = character
    return result

def montessori(text):
    vocals = 'aeiou'
    consonants = 'bcdfghjklmnpqrstvwxyz'
    text_list = list(text.lower())
    text_cyphered = ''
    for character in text_list:
        if vocals.find(character) >= 0:
            text_cyphered = text_cyphered + str(get_next_character_in_list
        (character,vocals))
        elif consonants.find(character) >= 0:
            text_cyphered = text_cyphered + str(get_next_character_in_list
        (character,consonants))
        else:
            text_cyphered = text_cyphered + character
    return text_cyphered


