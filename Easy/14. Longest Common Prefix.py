class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        prefix = ""
        if not strs:
            return prefix
        min_len = min([len(word) for word in strs])
        for idx in range(min_len):
            current = strs[0][idx]

            for s in strs:
                if s[idx] != current:
                    return prefix

            prefix += current

        return prefix

s = Solution()
