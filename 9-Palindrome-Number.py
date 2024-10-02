class Solution:
    def isPalindrome(self, x: int) -> bool:
        xstring = str(x)
        i = 0
        j = len(xstring) - 1
        while i < j:
            if xstring[i] != xstring[j]:
                return False
            i += 1
            j -= 1
        return True