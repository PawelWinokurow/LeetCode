from typing import List


class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        def is_correct(arr):
            i = 0
            while i < len(arr):
                if i == len(arr) - 1:
                    if arr[i] == 0:
                        return True
                    else:
                        return False
                if arr[i] == 1 and arr[i+1] == 0 or arr[i] == 1 and arr[i+1] == 1:
                    i += 2
                elif arr[i] == 0:
                    i+= 1
            return True 

        if bits[-1] == 0:
            return is_correct(bits[:-1])
        return False
