
# your code goes here!
class Anagram:
    def __init__(self, word):
        self.word = word.lower()

    def is_anagram(self, other_word):
        return sorted(self.word) == sorted(other_word.lower())

    def match(self, words):
        return [word for word in words if self.is_anagram(word)]
