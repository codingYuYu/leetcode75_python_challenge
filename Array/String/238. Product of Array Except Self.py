# 陣列乘積除自身問題（Product of Array Except Self）
# 這是該方法最直接的應用場景。題目要求計算每個元素，排除自身後的乘積，並避免使用除法

# 方法（Approach）:
#   前綴乘積（Prefix Products）:
#       從左到右遍歷陣列，計算每個元素之前的所有元素的乘積，並將這些結果存入一個名為 ans 的陣列中。
#   後綴乘積（Suffix Products）:
#       再從右到左遍歷陣列，將每個元素之後的所有元素的乘積，與 ans 陣列中的值相乘，完成最終結果。

# 這個方法的時間複雜度是O(n)，空間複雜度是O(1)

class Solution(object):
    def productExceptSelf(self, nums):
        n = len(nums)
        ans = [1] * n

        # Calculate prefix products
        for i in range(1,n):
            ans[i] = ans[i-1] * nums[i-1]

        # Calculate suffix products
        presuffix = 1
        for i in range(n-2,-1,-1):
            presuffix *= nums[i+1]
            ans[i] *= presuffix

        return ans
