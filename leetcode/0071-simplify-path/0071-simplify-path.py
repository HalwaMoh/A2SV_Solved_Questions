class Solution(object):
    def simplifyPath(self, path):
        stack=[]
        part=path.split("/")
        for i in part:
            if i=="" or i==".":
                continue
            elif i=="..":
                if stack:
                    stack.pop()
            else:
                stack.append(i)
        return  "/" + "/".join(stack)                


                    
 
        
        