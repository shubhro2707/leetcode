class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        target_to_num = {}
        for index, num in enumerate(nums):
            complement = target-num
            if complement in target_to_num:
                return [index, target_to_num[complement]]
            else:
                target_to_num[num] = index

        
        