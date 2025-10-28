class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        num_map = {}

        for idx, num in enumerate(nums):
            complement = target - num

            if complement in num_map:
                # возвращаем два индекса
                return [num_map[complement], idx]

            num_map[num] = idx

        return []


        