# Problem: Longest Word in Dictionary - https://leetcode.com/problems/longest-word-in-dictionary/

class TrieNode:
    def __init__(self):
        self.children = [None for _ in range(26)]
        self.is_end = False
        self.word_count = 0
class Solution:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        temp = self.root
        new_count = 0
        for c in word:
            i = ord(c) - 97
            if not temp.children[i]:
                if new_count < 1:
                    new_count += 1
                    temp.children[i] = TrieNode()
                else:
                    return False
            
            temp = temp.children[i]
        temp.is_end = True
        return True 
    def longestWord(self, words: List[str]) -> str:
        word_map = defaultdict(list)
        words.sort()
        print(words)
        for word in words:
            if word[0] not in words:
                continue
            correct = self.insert(word)
            if correct:
                word_map[len(word)].append(word)
        
        if len(word_map) > 0:
            max_key = max(word_map.keys())
            return min(word_map[max_key])
        else:
            return ""