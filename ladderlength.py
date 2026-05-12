from collections import deque

class Solution:
    def ladderLength(self, beginWord, endWord, wordList):
        wordSet = set(wordList)

        if endWord not in wordSet:
            return 0

        queue = deque()
        queue.append((beginWord, 1))

        while queue:
            word, level = queue.popleft()

            if word == endWord:
                return level

            for i in range(len(word)):
                for ch in "abcdefghijklmnopqrstuvwxyz":
                    newWord = word[:i] + ch + word[i + 1:]

                    if newWord in wordSet:
                        wordSet.remove(newWord)
                        queue.append((newWord, level + 1))

        return 0
