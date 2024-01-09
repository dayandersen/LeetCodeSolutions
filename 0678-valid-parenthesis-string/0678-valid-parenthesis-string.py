class Solution:
    def checkValidString(self, s: str) -> bool:
        open_stack = []
        ast_stack = []
        for i in range(len(s)):
            c = s[i]
            if c == "(":
                open_stack.append(i)
            elif c == ")":
                if open_stack:
                    open_stack.pop()
                elif ast_stack:
                    ast_stack.pop()
                else:
                    return False
            elif c == "*":
                ast_stack.append(i)
            else:
                continue
        
        while open_stack and ast_stack:
            if open_stack[-1] > ast_stack[-1]:
                return False
            open_stack.pop()
            ast_stack.pop()
        
        return not open_stack
