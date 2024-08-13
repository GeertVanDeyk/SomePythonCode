class Palindrome:

    @staticmethod
    def is_palindrome(word):
        return (word.upper() == word[::-1].upper())
   

print(Palindrome.is_palindrome('Deleveled'))
