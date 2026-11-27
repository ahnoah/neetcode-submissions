class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = dict()
        for str in strs:
            count = [0] * 26
            for letter in str:
                count[ord(letter) - ord('a')] += 1
            if tuple(count) not in groups:
                groups[tuple(count)] = [str]
            else:
                groups[tuple(count)].append(str)
        return list(groups.values())

