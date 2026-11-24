class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        output = [0] * len(temperatures)
        stack = [] #[(temp, index)]
        for i,n in enumerate(temperatures):
            while stack and n > stack[-1][0]:
                stacktemp, stackind = stack.pop()
                output[stackind] = (i - stackind)
            stack.append([n,i])
        return output

            