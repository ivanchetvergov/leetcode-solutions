class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        left, right = 0, len(nums) - 1
        
        while left <= right:
            mid = (left + right) // 2
            
            if nums[mid] == target:
                return mid
            
            # опред. какая половина отсорт
            if nums[left] <= nums[mid]:
                # --- левая пол отсорт ---
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else: 
                    left = mid + 1
            else:
                # --- правая половина ---
                if nums[mid] < target <= nums[right]:
                    left = mid + 1 
                else:
                    right = mid - 1
        
        return -1