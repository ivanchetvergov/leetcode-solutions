class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left, right = 0, len(height) - 1
        max_left, max_right = 0, 0
        collected_water = 0
        
        while (left < right):
            # левая гр ниже двигаем ее
            if (height[left] <= height[right]):
                # переопределим локальный максимум
                if (height[left] >= max_left):
                    max_left = height[left]
                # иначе добавим воды в наш пул
                else: 
                    collected_water += max_left - height[left]
                left += 1 # двигаем
                
            # есть правая сторона ниже двигаем ее
            else:
                # переопределим локальный максимум
                if (height[right] >= max_right):
                    max_right = height[right]
                # иначе добавим воды в наш пул
                else:
                    collected_water += max_right - height[right]
                right -= 1 # двигаем
        
        return collected_water
                            
            
