class Solution:
    def minOperations(self, nums: List[int]) -> int:
        flipqueue=deque()
        cnt=0
        for i in range(len(nums)):
            while flipqueue and i > flipqueue[0] +2:
                flipqueue.popleft()
            if( nums[i] + len(flipqueue)) % 2==0 :
                if i+2 >= len(nums):
                    return -1
                cnt +=1
                flipqueue.append(i)   
        return cnt


        