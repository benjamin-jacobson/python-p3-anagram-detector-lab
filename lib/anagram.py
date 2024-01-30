# your code goes here!
class Anagram:
    def __init__(self, word):
        self.word = word
        # sorted(str1) == sorted(str2)

    def match(self, list_of_words):
        matches =[]
        for i in list_of_words:
            if sorted(i) == sorted(self.word):
                matches.append(i)
        return matches