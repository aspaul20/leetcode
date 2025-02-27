class Solution:
    def minTimeToType(self, word: str) -> int:
        time = 0
        pointer = 0
        for char in word:
            target = ord(char) - ord('a')
            diff = abs(pointer - target)
            steps = min(diff, 26-diff)
            time += steps + 1
            pointer = target
        return time 
