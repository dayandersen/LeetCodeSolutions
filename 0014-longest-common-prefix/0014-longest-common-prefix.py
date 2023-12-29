class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        pos = 0
        while pos < len(strs[0]):
            letter = strs[0][pos]
            for strr in strs:
                if pos >= len(strr) or strr[pos] != letter:
                    return strs[0][:pos]
            pos += 1
        return strs[0][:pos]
