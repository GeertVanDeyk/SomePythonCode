import string

print("---- STRING CONSTANTS ----")
print()
print (" string.ascii_letters   : ", string.ascii_letters)
print (" string.ascii_lowercase : ", string.ascii_lowercase)
print (" string.ascii_uppercase : ", string.ascii_uppercase)
print (" string.digits          : ", string.digits)
print (" string.hexdigits       : ", string.hexdigits)
print (" string.octdigits       : ", string.octdigits)
print (" string.punctuation     : ", string.punctuation)
print (" string.whitespace      : ", string.whitespace)
print()
print()

sentence = 'A coward dies a 1000 times before his death, but the valiant taste of death but 1x.'
sentence_1 = '{} dies a 1000 times before his death, but {} taste of death but 1x.'
sentence_2 = '{argument2} dies a 1000 times before his death, but {argument1} taste of death but 1x.'
sentence_ascii_letters = ''
sentence_ascii_lowercase = ''
sentence_ascii_uppercase = ''
sentence_digits = ''
sentence_hexdigits = ''
sentence_octdigits = ''
sentence_punctuation = ''
sentence_printable = ''
sentence_whitespace = ''

for all_characters in sentence:
    if (all_characters in string.ascii_letters):
        sentence_ascii_letters = sentence_ascii_letters + all_characters
    if (all_characters in string.ascii_lowercase):
        sentence_ascii_lowercase = sentence_ascii_lowercase + all_characters
    if (all_characters in string.ascii_uppercase):
        sentence_ascii_uppercase = sentence_ascii_uppercase + all_characters
    if (all_characters in string.digits):
        sentence_digits = sentence_digits + all_characters       
    if (all_characters in string.hexdigits):
        sentence_hexdigits = sentence_hexdigits + all_characters  
    if (all_characters in string.octdigits):
        sentence_octdigits = sentence_octdigits + all_characters
    if (all_characters in string.punctuation):
        sentence_punctuation = sentence_punctuation + all_characters
    if (all_characters in string.printable):
        sentence_printable = sentence_printable + all_characters
    if (all_characters in string.whitespace):
        sentence_whitespace = sentence_whitespace + all_characters
print('E.g. : ', sentence)
print()
print('ascii_letters : ',sentence_ascii_letters)        
print('ascii_lowercase : ',sentence_ascii_lowercase)
print('ascii_uppercase : ',sentence_ascii_uppercase)
print('digits : ',sentence_digits)
print('hexdigits : ',sentence_hexdigits)
print('octdigits : ',sentence_octdigits)
print('punctuation : ',sentence_punctuation)
print('printable : ',sentence_printable)
print('whitespace : ',sentence_whitespace)
print()
print("---- str.format ----")
print()
print('E.g. : ',sentence_1)
print('''sentence_1.format('an elephant', 'a bird') : ''',sentence_1.format('an elephant', 'a bird'))
print('E.g. : ',sentence_2)
print('''sentence_2.format(argument2='the man', argument1='the woman') : ''',sentence_2.format(argument2='the man', argument1='the woman'))
print()
print("---- HELPER FUNCTIONS ----")
print()
print('string.capwords : ', string.capwords(sentence))
