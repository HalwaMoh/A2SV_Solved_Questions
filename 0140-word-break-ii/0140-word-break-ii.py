class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        wordset=set(wordDict)
        res=[]
        curr=[]
        self.backtrack(s,wordset,[],res,0)
        return res
    def backtrack(self,s,wordset,curr,res,start):
        if start==len(s):
            res.append(" ".join(curr))
            return res
        for end in range(start+1 , len(s)+1):
            word=s[start : end]
            if word in wordset:
                curr.append(word)
                self.backtrack(s,wordset,curr,res,end)
                curr.pop()


    
    