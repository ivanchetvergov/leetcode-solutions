class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        value = int(''.join(str(el) for el in digits))
        value += 1
        
        result = [int(el) for el in str(value)]
        
        return result