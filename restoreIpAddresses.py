class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        result = []
        def backtrack(all_segs, start, segments):
            
            if segments == 0 and start == len(s):
                result.append(all_segs)
                return 

            for i in range(start, min(start+3, len(s))):
                segment = s[start:i+1]
                if len(segment) > 1 and segment.startswith('0'):
                    continue 
                segment = int(segment)
                if segment >= 0 and segment <= 255 :
                    new_segs = all_segs + str(segment) + ('.' if segments > 1 else '')
                    backtrack(new_segs, i+1, segments-1)

        backtrack('', 0, 4)
        return result
