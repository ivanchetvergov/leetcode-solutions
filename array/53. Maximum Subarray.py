class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        ! классический жадный алгос
        идея в том чтобы следить за локальным
        и глобальным максимум
        и резать локальный если он меньше нового эл
        """
        N = len(nums)
        if N == 0:
            return 0
        
        glob_max = nums[0]
        local_max = nums[0]
        
        for i in range(1, N):
            cur_num = nums[i]
            
            # * правило Кадана: начать новый или тянуть старый?
            # определяем локальный максимум
            local_max = max(cur_num, local_max + cur_num)
            # глобальный максимум
            glob_max = max(glob_max, local_max)
            
        return glob_max