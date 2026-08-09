class Solution:
    def wordPattern(self, pattern, s):

        words = s.split()

        if len(pattern) != len(words):
            return False

        map1 = {}
        map2 = {}

        for i in range(len(pattern)):

            a = pattern[i]
            b = words[i]

            if a in map1 and map1[a] != b:
                return False

            if b in map2 and map2[b] != a:
                return False

            map1[a] = b
            map2[b] = a

        return True
