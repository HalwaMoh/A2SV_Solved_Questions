class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        self.count = 0
        self.ans = ""

        def backtrack(path):
            if len(path) == n:
                self.count += 1
                if self.count == k:
                    self.ans = path
                return

            for ch in "abc":
                if not path or path[-1] != ch:
                    if self.ans:  
                        return
                    backtrack(path + ch)

        backtrack("")
        return self.ans