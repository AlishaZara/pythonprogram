class AnilInterrupt(Exception):
    pass

a=input('enter a string:- ')
if a[0] in 'aeiouAEIOU':
    raise AnilInterrupt('first char should not be a vowel')
                        