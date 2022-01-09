from typing import List


class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        s = [set('qwertyuiop'), set('asdfghjkl'), set('zxcvbnm')]
        ans = []
        for i in range(3):
            for word in words:
                if set(word.lower()).intersection(s[i]) == set(word.lower()):
                    ans.append(word)
        return ans
