class Solution(object):
    def groupAnagrams(self, strs):
        anagrams = {}  

        for word in strs:
            
            key = ''.join(sorted(word))
            
           
            if key in anagrams:
                anagrams[key].append(word)
            else:
                anagrams[key] = [word]

        
        return list(anagrams.values())
