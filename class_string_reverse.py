class ReverseString:

    def reverse_words(self, text):
        words = text.split()
        words.reverse()
        result = " ".join(words)
        return result


obj = ReverseString()

sentence = input("Enter a sentence: ")

print("Reversed sentence:", obj.reverse_words(sentence))