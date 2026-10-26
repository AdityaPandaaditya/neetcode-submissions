class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        seen = {}

        for index, num in enumerate(numbers):
            balance = target - num

            if balance in seen :
                return sorted([index+1 , seen[balance]+1])

            seen[num] = index

    