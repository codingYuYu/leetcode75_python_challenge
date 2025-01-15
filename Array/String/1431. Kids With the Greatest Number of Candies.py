class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        ans = []
        x = max(candies)
        for i in range(len(candies)):
            ans.append(True) if ((candies[i] + extraCandies) >= x) else ans.append(False)
        return ans