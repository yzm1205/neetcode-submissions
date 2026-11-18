from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        word_dict = defaultdict(list)

        for word in strs:
            word_vector = [0]*26
            for i in word:
                word_vector[ord(i) - ord('a')] += 1   
            word_dict[tuple(word_vector)].append(word)
        
        return list(word_dict.values())

            
            


        