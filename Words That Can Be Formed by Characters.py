class Solution(object):
    def countCharacters(self, words, chars):
        total = 0
        
        for word in words:
            count = {}
            for c in chars:
                count[c] = count.get(c, 0) + 1
            
            good = True
          
            for c in word:
                if count.get(c, 0) == 0:
                    good = False
                    break
                count[c] -= 1
            
            if good:
                total += len(word)
        
        return total
