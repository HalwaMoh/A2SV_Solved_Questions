
from collections import deque
class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        graph=[[] for _ in range(numCourses)]
        order=[]
        queue=deque()
        incoming=[0   for _ in range(numCourses) ]
        for course ,pre in prerequisites:
            graph[pre].append(course)
            incoming[course] +=1
        for course in range(numCourses):

            if incoming[course] == 0:
                queue.append(course)
        
        while queue:
            course=queue.popleft()
            order.append(course)

            for neghibor in graph[course]:
                incoming[neghibor] -=1
                
                if incoming[neghibor] == 0:
                    queue.append(neghibor)
        if len(order) != numCourses:
            return []   
        return order             
        
        