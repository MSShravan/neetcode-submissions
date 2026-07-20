class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for t in tokens:
            if t == '+':
                tmp = stack.pop() + stack.pop()
                stack.append(tmp)
            elif t == '-':
                l = stack.pop()
                r = stack.pop()
                tmp = r - l
                stack.append(tmp)
            elif t == '*':
                tmp = stack.pop() * stack.pop()
                stack.append(tmp)
            elif t == '/':
                l = stack.pop()
                r = stack.pop()
                tmp = int(r / l)
                stack.append(tmp)
            else:
                stack.append(int(t))
        return stack[-1]