from typing import List


class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        codes = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.", "---",
         ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]
        codes = {chr(i+97): code for i, code in enumerate(codes)}
        words = [list(word) for word in words]
        return len(set([''.join(map(codes.get, word)) for word in words]))
