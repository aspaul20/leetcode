class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        letters = 'qwertyuiopasdfghjklzmxncbv'
        dictionary = {char:0 for char in letters}
        dictionary.update({char:0 for char in letters.upper()}) 

        for char in s:
            dictionary[char] += 1 
        non_zero = [elem for key, elem in dictionary.items() if elem > 0]
        return len(set(non_zero)) == 1
        
