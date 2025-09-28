class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        N = len(nums)
        best_sum = nums[0] + nums[1] + nums[2]
        
        min_dist = abs(best_sum - target)
        
        for i in range(N - 2):
            a = nums[i]
            left, right = i + 1, N - 1
            
            while left < right: 
                
                cur_sum = a + nums[left] + nums[right]
                cur_dist = abs(cur_sum - target)
                
                if cur_dist < min_dist:
                    min_dist = cur_dist
                    best_sum = cur_sum
                
                                
                if cur_sum == target:
                    return cur_sum
                
                elif cur_sum < target:
                    left += 1
                else:
                    right -= 1
                    
        return best_sum
     