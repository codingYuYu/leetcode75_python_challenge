class Solution(object):
    def isSubsequence(self, s, t):
        if len(t) < len(s):
            return False
        if len(s) == 0:
            return True
        p = 0
        subsequence = len(s)
        for i in t:
            if s[p]==i:
                p+=1
            if p == subsequence:
                return True
        return False
