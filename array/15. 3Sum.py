class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        result = []
        N = len(nums)
        
        for i in range(N):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            a = nums[i]
            left, right = i + 1, N - 1
            
            # (b + c) = - a
            while left < right:
                b = nums[left]
                c = nums[right]
                current_sum = a + b + c
                
                if current_sum == 0: 
                    result.append([a, b, c])
                    
                    left +=1
                    right -=1
                    
                    # пропускаем дубликаты
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                    
                elif current_sum < 0:
                    left += 1
                elif current_sum > 0:
                    right -= 1
        
        return result 