class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        left = 0
        max_lenght = 0
        char_set = set()
        
        for right in range(len(s)):
            # ! удаляем эл-ты пока не удалим новый
            while s[left] in char_set:
                char_set.remove(s[left])
                left += 1
                
            char_set.add(s[right]) # добавляем новый элемент
            # пересчет
            max_lenght = max(max_lenght, right - left + 1)
            
        return max_lenght
            