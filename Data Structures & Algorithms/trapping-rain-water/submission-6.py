class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        l, r = 0, len(height) - 1
        maxLeft = height[l]
        maxRight = height[r]
        response = 0

        while l < r:
            if maxLeft <  maxRight:
                l += 1
                maxLeft = max(maxLeft, height[l])
                response += max(0, maxLeft-height[l])

            else:
                r-=1
                maxRight = max(maxRight, height[r])
                response += max(0, maxRight-height[r])

        return response
        
