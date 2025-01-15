class Solution(object):
    def mergeAlternately(self, word1, word2):
        ans = ""
        time = max(len(word1),len(word2))
        for i in range(time):
            if i < len(word1):
                ans += word1[i]
            if i < len(word2):
                ans += word2[i]
        return ans
