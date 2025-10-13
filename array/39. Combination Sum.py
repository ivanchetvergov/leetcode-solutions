class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        results = []
        
        def _backtrack(
            target_left, # сколько до таргета
            start_idx, 
            curr_comb
        ):
            # 1 --- базовый случай
            if (target_left == 0):
                results.append(list(curr_comb))
                return
            
            # 2 --- обработка выхода за таргет
            elif (target_left < 0):
                return
            
            # 3 --- основной рекурсивный шаг
            for i in range(start_idx, len(candidates)):
                candidate = candidates[i]
                
                # базовая проверка
                if candidate > target_left:
                    break
                
                # добавляем эл в послед
                curr_comb.append(candidate)
                # вызываем рекурсию
                _backtrack(
                    target_left - candidate,
                    i, 
                    curr_comb
                )
                # удаляем число, чтобы перебрать остальные
                curr_comb.pop()
                
        _backtrack(target, 0, [])
        return results