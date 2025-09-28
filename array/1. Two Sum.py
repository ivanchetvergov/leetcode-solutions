class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        # {num : idx}
        num_map = {}
        
        for idx, num in enumerate(nums):
            # вычисляем дополнение
            complement = target - num
            
            if complement in num_map:
                return [num_map[complement], idx]
            
            num_map[num] = idx
        
        return []
            
            