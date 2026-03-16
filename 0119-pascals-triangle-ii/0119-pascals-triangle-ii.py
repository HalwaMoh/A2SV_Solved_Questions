class Solution(object):
    def getRow(self, rowIndex):
        if rowIndex==0:
            return [1]
        curr_row=[1]
        pre_row=self.getRow(rowIndex-1)
        
        for i in range(1,rowIndex):
            curr_row.append(pre_row[i] +  pre_row[i-1])
        curr_row.append(1)    
        return curr_row      
        