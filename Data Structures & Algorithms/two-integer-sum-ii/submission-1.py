class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        seen = {}

        for index, num in enumerate(numbers):
            balance = target - num

            if balance in seen :
                return ([seen[balance]+1,index+1])

            seen[num] = index

    