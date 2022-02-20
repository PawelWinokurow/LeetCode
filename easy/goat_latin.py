
class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        words = sentence.split(' ')
        for i, word in enumerate(words):
            if word[0] not in 'AaEeIiOoUu':
                words[i] = words[i][1:] + words[i][0]
            words[i] += 'ma' + 'a' * (i+1)
        return ' '.join(words)