class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count_m = {}
        count_n = {}

        for ch in s:
            if ch in count_m:
                count_m[ch] += 1
            
            else:
                count_m[ch] = 1
        
        for ch in t:
            if ch in count_n:
                count_n[ch] += 1
            
            else:
                count_n[ch] = 1
        if count_m == count_n:
            return True
        else:
            return False
        
        
            
