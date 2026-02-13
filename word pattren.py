class Solution(object):
    def wordPattern(self, pattern, s):
        words = s.split()
        if len(pattern) != len(words):
            return False
        pattern_s = {}
        s_pattern = {}
        
        for c, w in zip(pattern, words):
            if c in pattern_s:
                if pattern_s[c] != w:
                    return False
            else:
                pattern_s[c] = w
            if w in s_pattern:
                if s_pattern[w] != c:
                    return False
            else:
                s_pattern[w] = c
        
        return True
