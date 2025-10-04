class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """

        N = len(nums)
        
        # --- 1 ищем pivot
        i = N - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1

        # --- 2 ищем число для перестановки        
        if i >= 0:
            j = N - 1
            while nums[j] <= nums[i]:
                j -= 1
                
            nums[i], nums[j] = nums[j], nums[i]
            
        # --- 3 реверс суффикса
        start = i + 1
        end = N - 1
        
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1