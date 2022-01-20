class Solution:
    def judgeCircle(self, moves: str) -> bool:
        a = [0, 0, 0, 0]
        for c in moves:
            if c == 'U':
                a[0] += 1
            elif c == 'D':
                a[1] += 1
            elif c == 'L':
                a[2] += 1
            elif c == 'R':
                a[3] += 1
        return a[0] == a[1] and a[2] == a[3]