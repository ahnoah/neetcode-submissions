class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        keys = dict()
        for str in strs:
            alphabetized = "".join(sorted(str))
            if alphabetized in keys:
                keys[alphabetized].append(str)
            else:
                keys[alphabetized] = [str]
            
        return list(keys.values())

