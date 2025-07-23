class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        k = {}
        if len(s) < 10:
            return []

        new = []
        there = set()
        for i in range(len(s)-9):
            if s[i:i+10] in there:
                new.append(s[i:i+10])
            else:
                there.add(s[i:i+10])
        return list(set(new))


        