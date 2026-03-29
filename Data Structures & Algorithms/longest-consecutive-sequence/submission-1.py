class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #start when n-1 not in nums
        #keep on looking for n+1.. until we run out... set longest
        #pick the other .. recompute.. reassign .. longest if satisfoes
        hashSet = Counter(nums)
        longest = 0 
        l  = 1
        for i in nums:
            if i-1 not in hashSet:
                #startCounter
                currLong = 1
                while i + currLong in hashSet:
                    currLong+=1
                longest = max(longest, currLong)
        return longest