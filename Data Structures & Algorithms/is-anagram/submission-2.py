from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False
        anagram = defaultdict(int)
        for ch in s :
            anagram[ch] += 1
        for ch in t : 
            anagram[ch] -= 1 
        
        for val in anagram.values():
            if val != 0:
                return False 
        return True
        
        