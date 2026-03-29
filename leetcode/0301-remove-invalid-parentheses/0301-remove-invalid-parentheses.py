class Solution(object):
    def removeInvalidParentheses(self, s):
        ans = set()
        l = r = 0
        for ch in s:
            if ch == '(':
                l += 1
            elif ch == ')':
                if l == 0:
                    r += 1
                else:
                    l -= 1

        def dfs(i, path, open_cnt, l, r):
            if i == len(s):
                if open_cnt == 0 and l == 0 and r == 0:
                    ans.add(path)
                return

            ch = s[i]

           
            if ch == '(' and l > 0:
                dfs(i + 1, path, open_cnt, l - 1, r)
            elif ch == ')' and r > 0:
                dfs(i + 1, path, open_cnt, l, r - 1)

            
            if ch not in '()':
                dfs(i + 1, path + ch, open_cnt, l, r)
            elif ch == '(':
                dfs(i + 1, path + ch, open_cnt + 1, l, r)
            elif ch == ')' and open_cnt > 0:
                dfs(i + 1, path + ch, open_cnt - 1, l, r)

        dfs(0, "", 0, l, r)
        return list(ans)
        