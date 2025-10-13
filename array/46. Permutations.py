class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        result = []
        N = len(nums)
        used = [False] * N
        
        def _backtrack(curr_perm):
            # 1 --- базовый случай
            if len(curr_perm) == N:
                result.append(list(curr_perm)) # добавляем копию
                return None
            
            # 2 --- рекурсивный шаг
            for i in range(N):
                
                #  если эл есть то скип
                if used[i]:
                    continue
                
                # A) делаем выбор (choose)
                candidate = nums[i]
                curr_perm.append(candidate)
                used[i] = True # помечаем эл
                
                # B) след шаг (explore)
                _backtrack(curr_perm)

                # C) отмена шага (unchoose/backtrack)
                used[i] = False
                curr_perm.pop()
                
        _backtrack([])
        return result
                