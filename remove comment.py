class Solution(object):
    def removeComments(self, source):
       
        in_block = False       
        new_source = []        
        buffer = ""            

        for line in source:
            i = 0
            while i < len(line):
                if not in_block and line[i:i+2] == "/*":
                    in_block = True
                    i += 2  
                elif in_block and line[i:i+2] == "*/":
                    in_block = False
                    i += 2 
                elif not in_block and line[i:i+2] == "//":
                    break    
                elif not in_block:
                    buffer += line[i]
                    i += 1
                else:
                    i += 1  

            if buffer and not in_block:
                new_source.append(buffer)
                buffer = ""

        return new_source

        
