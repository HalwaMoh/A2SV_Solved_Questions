class Solution(object):
    def findDuplicate(self, paths):
        content_map = {}  

        for path in paths:
            parts = path.split(" ")
            folder = parts[0] 

            
            for file_info in parts[1:]:
                
                name, content = file_info.split("(")
                content = content[:-1] 
                full_path = folder + "/" + name
                if content in content_map:
                    content_map[content].append(full_path)
                else:
                    content_map[content] = [full_path]

       
        return [group for group in content_map.values() if len(group) > 1]
