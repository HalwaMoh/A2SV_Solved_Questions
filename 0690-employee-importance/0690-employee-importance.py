"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        hashmap={}
        for employee in employees:
            hashmap[employee.id]= [employee.importance, employee.subordinates]
        cnt=0    
        def dfs(idd):
            nonlocal cnt
            val = hashmap[idd] #[5,[2,3]]
            cnt += val[0]
            if val[1]:
                for i in val[1]:
                    dfs(i)
                
        for emp in employees:
            if emp.id==id:
                dfs(emp.id)
                return cnt        




        