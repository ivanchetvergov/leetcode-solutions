class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left = 0
        right = len(height) - 1
        max_area = 0
        
        while left != right:
            h_left = height[left]
            h_right = height[right]
            curr_height = min(h_left, h_right)
            
            width = right - left
            curr_height = width * curr_height
            
            max_area = max(max_area, curr_height)
            
            if h_left < h_right:
                left += 1
            else:
                right -= 1
        
        return max_area