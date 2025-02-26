class Solution:
    def getLucky(self, s: str, k: int) -> int:
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        mapping = {char: ord(char)-96 for char in alphabet}
        num_str = "".join([str(mapping[char]) for char in s])

        _sum = sum([int(num) for num in num_str])
        for _ in range(k-1): 
            _sum = sum([int(num) for num in str(_sum)])
        return _sum
        
