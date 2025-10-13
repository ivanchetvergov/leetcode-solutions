class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        N = len(nums)
        if N <= 1: return 0
        
        jumps = 0
        curr_end = 0
        max_range = 0
        
        for i in range(N - 1):
            # 1 --- ищем новую макс границы
            max_range = max(max_range, i + nums[i])
            
            # 2 --- проверяем достигли ли пред. границы
            if i == curr_end:
                # увелич счетчик прыжков 
                jumps += 1
                # обновляем границы
                curr_end = max_range
                # допрыгались
                if curr_end >= N - 1:
                    break
                
        return jumps