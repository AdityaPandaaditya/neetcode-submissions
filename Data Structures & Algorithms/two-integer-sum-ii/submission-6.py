class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        result = []
        numbers.sort()
        
        l, r = 0, len(numbers) - 1

        while l < r:
            total = numbers[l] + numbers[r]
            if total > target:
                r -= 1
            elif total < target:
                l += 1
            else:
                return [l+1, r+1]

        











    

    # seen = {}

    #     for index, num in enumerate(numbers):
    #         balance = target - num

    #         if balance in seen :
    #             return ([seen[balance],index+1])

    #         seen[num] = index +1

    