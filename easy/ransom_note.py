import collections


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
            # ransomNote = sorted(ransomNote)
            # magazine = sorted(magazine)
            # i = j = 0
            # while i < len(ransomNote) and j < len(magazine):
            #     a = magazine[j]
            #     if ransomNote[i] == magazine[j]:
            #         i += 1
            #         j += 1
            #     elif ransomNote[i] < magazine[j]:
            #         return False
            #     else:
            #         j += 1
            # return not (j == len(magazine) and i < len(ransomNote))
        a = collections.Counter(ransomNote)
        b = collections.Counter(magazine)
        c = a - b
        return not c