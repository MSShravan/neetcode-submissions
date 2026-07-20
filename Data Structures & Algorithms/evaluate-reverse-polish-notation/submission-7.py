class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        def dfs():
            t = tokens.pop()
            if t not in "+-*/":
                return int(t)
            
            r = dfs()
            l = dfs()

            if t == '+':
                return l + r
            elif t == '-':
                return l - r
            elif t == '*':
                return l * r
            else:
                return int(l/r)

        return dfs()