# Link: https://leetcode.com/problems/find-words-containing-character/

def findWordsContaining(words, x):
    """
    :type words: List[str]
    :type x: str
    :rtype: List[int]
    """
    return [i for i, word in enumerate(words) if x in word]

if __name__ == "__main__":
    print(findWordsContaining(["abc","bcd","aaaa","cbc"], "a"))