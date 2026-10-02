class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        i = 0
        while i <= len(nums) - 1:
            diff = target - nums[i]
            if diff in seen:
                return [seen[diff], i]
            else:
                seen[nums[i]] = i
            i += 1






        
        # while i <= len(nums) - 1:
        #     j = i + 1
        #     while j <= len(nums) - 1:
        #         if nums[i] + nums[j] == target:
        #             return [i, j]
        #         else:
        #             j += 1
        #     i += 1
