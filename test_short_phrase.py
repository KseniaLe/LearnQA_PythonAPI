import requests


phrase = input("Set a phrase: ")
print(phrase)
number_of_char = len(phrase)
print(number_of_char)

class Test_phrase:
    def test_short_phrase(self):
        a = number_of_char
        b = 15

        assert a < b, "The phrase is longer than 15 characters"