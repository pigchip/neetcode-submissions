class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        l = 0
        r = len(nums) - 1

        nums.sort()

        while l < r:
            if nums[l] == nums[r]:
                return True
            elif nums[l] < nums[r]:
                l += 1
            else:
                r -= 1
        
        return False
        