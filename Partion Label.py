class Solution(object):
    def partitionLabels(self, s):
        start=0
        end=0
        freq={}
        res=[]
        for i,ch in enumerate(s):
            freq[ch]= i
        for i,ch in  enumerate(s):
           
            end=max(end,freq[ch])
            if i == end:
                res.append(i-start +1)
                start=i +1
        return res        




       

        
        
