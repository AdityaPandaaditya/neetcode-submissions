class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return (self.sort_str(s) == self.sort_str(t))

    def sort_str(self, s):
        sorted_str = ''.join(sorted(s))
        return sorted_str
        