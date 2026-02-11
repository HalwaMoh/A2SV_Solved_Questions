class Solution(object):
    def closeStrings(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: bool
        """
        for ch1 in word1:
            if ch1 in word2 and len(word1)==len(word2):
                 return True
            else:
                return False     
            
