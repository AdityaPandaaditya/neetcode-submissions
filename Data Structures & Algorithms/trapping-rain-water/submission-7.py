class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0

        l,r = 0, len(height)-1
        maxLeft = height[l]
        maxRight = height[r]
        result = 0

        while l < r:
            if maxLeft < maxRight:
                l += 1
                water = maxLeft - height[l]
                result += max(0,water)
                maxLeft = max(height[l], maxLeft)
            else:
                r -= 1
                water = maxRight - height[r]
                result += max(0,water)
                maxRight = max(height[r], maxRight)
        return result
