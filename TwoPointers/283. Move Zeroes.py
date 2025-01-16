class Solution(object):
    def moveZeroes(self, nums):
        p1 = 0
        p2 = 1
        n = len(nums)
        while p2 < n:
            if nums[p1] == 0:
                if nums[p2] != 0:
                    nums[p1],nums[p2] = nums[p2],nums[p1]
                else:
                    p2+=1
            else:
                p1+=1
                p2+=1
        return nums