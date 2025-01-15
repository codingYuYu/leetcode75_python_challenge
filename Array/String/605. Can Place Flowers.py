class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        count = 0
        flowerbed =  [0] + flowerbed +[0]
        for i in range(1,len(flowerbed)-1):
            if flowerbed[i-1]==0 and flowerbed[i] == 0 and flowerbed[i+1]==0:
                count+=1
                flowerbed[i] = 1
            if count >= n:
                return True
        return False