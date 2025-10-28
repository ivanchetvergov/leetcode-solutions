class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        N = len(s)
        if N < 2:
            return s
        
        longest_p = ""
        
        # * 1 вспомогательная функция для расширения
        def _expand_around_center(l, r):
            """Расширяет границы (l, r) пока это палиндром и возвращает его."""
            while l >= 0 and r < N and s[l] == s[r]:
                l -= 1
                r += 1
            return s[l + 1: r]

        # * 2 перебор всех 2N - 1 центров
        for i in range(N):
            
            # центр 1: нечётная длина (например, 'a' или 'b a b')
            p1 = _expand_around_center(i, i) 
            if len(p1) > len(longest_p):
                longest_p = p1
            
            # центр 2: четная длина (например, 'aa' или 'b aa b')
            p2 = _expand_around_center(i, i + 1)
            if len(p2) > len(longest_p):
                longest_p = p2
                
        return longest_p