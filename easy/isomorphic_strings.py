class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        rep_s_t = {}
        rep_t_s = {}
        for i in range(len(s)):
            if s[i] not in rep_s_t and t[i] not in rep_t_s:
                rep_s_t[s[i]] = t[i]
                rep_t_s[t[i]] = s[i]
            elif s[i] not in rep_s_t and t[i] in rep_t_s \
                    or s[i] in rep_s_t and t[i] not in rep_t_s \
                    or rep_s_t[s[i]] != t[i] or rep_t_s[t[i]] != s[i]:
                return False
        return True
