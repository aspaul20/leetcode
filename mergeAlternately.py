class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result = []
        min_len = min(len(word1),len(word2))
        for i in range(min_len):
            result.append(word1[i])
            result.append(word2[i])
        
        result.extend(word1[i+1:])
        result.extend(word2[i+1:])

        return "".join(result)











        # merged_str = ''
        # for i in range(min(len(word1), len(word2))):
        #     merged_str += (word1[i])
        #     merged_str += (word2[i])

        # if len(word1) > len(word2):
        #     merged_str+=word1[i+1:]
        # elif len(word1) < len(word2):
        #     merged_str+=word2[i+1:]
        # return merged_str
