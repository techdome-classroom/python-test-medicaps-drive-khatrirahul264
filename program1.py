class Solution(object):
    def isValid(self, s):
        stack=[]
        brackets_map={')':'(',']':'[','}':'{'}
        for char in s:
            if char in brackets_map.values():
                stack.append(char)
            elif char in brackets_map.keys():
                if not stack or brackets_mp[char] != stack.pop():
                    return False
            else:
                return False

         return not stack

solution=Solution()
print(solution.isValid("(())[]{}"))
    



  

