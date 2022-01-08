class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        s = s.replace('-', '').upper()
        s_ = [s[:len(s) % k]] if len(s) % k > 0 else []
        for i in range(len(s) // k):
            s_.append(s[len(s) % k + i * k:len(s) % k + (i+1) * k])
        return '-'.join(s_)