class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        @cache
        def recurse(remaining_word):
            if len(remaining_word) == 0:
                return True
            found_match = False
            for word in wordDict:
                if remaining_word.startswith(word):
                    found_match = found_match or recurse(remaining_word[len(word):])
            return found_match
        return recurse(s)