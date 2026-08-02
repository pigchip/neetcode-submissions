class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        s = set(nums)

        if s.len() != nums.len():
            return True
        else:
            return False
        