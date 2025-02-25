class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs = sorted(strs)
        prefix = ''
        first = strs[0]
        last = strs[-1]
        for i in range(min(len(first), len(last))):
            char_f = first[i]
            char_l = last[i]
            if char_f != char_l:
                return prefix 
            else:
                prefix = prefix + char_f
        return prefix
