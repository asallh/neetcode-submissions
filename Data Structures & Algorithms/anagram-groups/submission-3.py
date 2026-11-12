class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Group all anagrams into subliusts
        res = defaultdict(list)  # Mapping the charCount to List of Anagrams

        for words in strs:
            count = [0] * 26

            for c in words:
                count[ord(c) - ord("a")] += 1

            res[tuple(count)].append(words)

        return list(res.values())