class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i,nums in enumerate(nums):
            diff = target - nums

            if diff in hashmap :
                return [hashmap[diff],i]
            hashmap[nums] = i
        


        