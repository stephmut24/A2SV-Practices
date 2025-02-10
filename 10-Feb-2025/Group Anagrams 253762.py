# Problem: Group Anagrams - https://leetcode.com/problems/group-anagrams/

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)

        for word in (strs):
            sorted_word = ''.join(sorted(word))
            groups[sorted_word].append(word)
        
        return list(groups.values())
        