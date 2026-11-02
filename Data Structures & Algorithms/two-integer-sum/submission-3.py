class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        prevMap = {}

        for inx, num in enumerate(nums):
            diff = target - num
            if diff in prevMap:
                return [prevMap[diff], inx]
            prevMap[num] = inx