class Solution:
    def isPrefixString(self, s: str, words: List[str]) -> bool:
        current_word_str = ''
        for word in words:
            current_word_str += word 
            if current_word_str == s:
                return True
        return False 
