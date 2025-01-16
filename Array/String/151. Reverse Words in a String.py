class Solution(object):
    def reverseWords(self, s):
        head = 0
        tail = len(s)
        word = []

        while head < tail:
            if head == ' ':
                head+=1
            if tail == ' ':
                tail-=1
            if head != ' ' and tail != ' ':
                s = s[head:tail+1]
                break

        word = s.split()
        ans = []

        for i in range(len(word)-1,-1,-1):
            ans.append(word[i])
        return " ".join(ans)
