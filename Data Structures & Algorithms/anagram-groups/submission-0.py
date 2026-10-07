class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = {}
        for word in strs:
            ch_arr = [0] * 26
            for ch in word:
                ch_arr[ord(ch) - ord('a')] += 1
            key = tuple(ch_arr)
            if key in seen:
                seen[key].append(word)
            else:
                seen[key] = [word]
        return list(seen.values())
        