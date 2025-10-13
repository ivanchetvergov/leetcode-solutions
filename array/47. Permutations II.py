class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        nums.sort() 
        results = []
        N = len(nums)
        used = [False] * N
        
        def _backtrack(curr_perm):
            # 1 --- базовый случай
            if len(curr_perm) == N:
                results.append(list(curr_perm)) # добавляем копию
                return None
            
            # 2 --- рекурсивный шаг
            for i in range(N):
                
                # проверка использования
                if used[i]:
                    continue
                
                # устранение дубликатов
                # not used[i - 1] проверяет что прошлое число еще не юзалось
                if i > 0 and nums[i] == nums[i - 1] and not used[i - 1]:
                    continue
                
                # A) делаем выбор (choose)
                candidate = nums[i]
                used[i] = True
                curr_perm.append(candidate)
    
                
                # B) след шаг (explore)
                _backtrack(curr_perm)

                # C) отмена шага (unchoose/backtrack)
                used[i] = False
                curr_perm.pop()
                
        _backtrack([])
        return results