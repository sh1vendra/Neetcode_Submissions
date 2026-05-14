class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    
        d = {}
        for word in strs:
            sorted_letters= sorted(word)
            sorted_word = ''.join(sorted_letters)
            if sorted_word not in d:
                d[sorted_word] = []
            d[sorted_word].append(word)
        return list(d.values())
            