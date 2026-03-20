class Solution(object):
    def groupThePeople(self, groupSizes):
        group={}
        ans=[]
        for i in range(len(groupSizes)):
            if groupSizes[i] in group:
                group[groupSizes[i]].append(i)
            else:
                group[groupSizes[i]]=[i] 
        for i,j in group.items():
            if i==len(j):
                ans.append(j)
            else:
                l=[]  
                for k in j:
                    l.append(k)
                    if len(l)==i:
                        ans.append(l)
                        l=[]
                   
        return ans                


                         


        
        