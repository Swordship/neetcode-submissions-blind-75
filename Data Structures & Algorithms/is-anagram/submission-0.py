class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s1 = ''.join(sorted(s))
        t1 = ''.join(sorted(t))

        if s1.lower() == t1.lower():
            return True
        else :
            return False 