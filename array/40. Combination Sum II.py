class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        results = set()
        
        def _backtrack(
            target_left, # сколько до таргета
            start_idx, 
            curr_comb
        ):
            # 1 --- базовый случай
            if (target_left == 0):
                results.add(tuple(curr_comb))
                return
            
            # 2 --- обработка выхода за таргет
            elif (target_left < 0):
                return
            
            # 3 --- основной рекурсивный шаг
            for i in range(start_idx, len(candidates)):
                candidate = candidates[i]
                
                # проверка дубликатов
                if i > start_idx and candidates[i] == candidates[i - 1]:
                    continue
                
                # ранний выход
                if candidate > target_left:
                    break 
                
                # добавляем эл в послед
                curr_comb.append(candidate)
                # вызываем рекурсию
                _backtrack(
                    target_left - candidate,
                    i + 1, 
                    curr_comb
                )
                # удаляем число, чтобы перебрать остальные
                curr_comb.pop()
                
        _backtrack(target, 0, [])
        return [list(comb) for comb in results]