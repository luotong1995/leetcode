'''
给定一个字符串 s 和一个字符串字典 wordDict ，在字符串 s 中增加空格来构建一个句子，使得句子中所有的单词都在词典中。以任意顺序 返回所有这些可能的句子。

注意：词典中的同一个单词可能在分段中被重复使用多次。


输入:s = "catsanddog", wordDict = ["cat","cats","and","sand","dog"]
输出:["cats and dog","cat sand dog"]


输入:s = "pineapplepenapple", wordDict = ["apple","pen","applepen","pine","pineapple"]
输出:["pine apple pen apple","pineapple pen apple","pine applepen apple"]
解释: 注意你可以重复使用字典中的单词。
'''


def wordBreak(s, wordDict):
    """
    :type s: str
    :type wordDict: List[str]
    :rtype: List[str]
    """
    re = []
    splitStr(s, wordDict, [], re)
    return list(set(re))


def splitStr(s, wordDict, result_list, re):
    for item in wordDict:
        if s.startswith(item):
            result_list.append(item)
            splitStr(s[len(item):], wordDict, result_list, re)
            result_list.remove(item)
        if s == '':
            a = ' '.join(result_list)
            re.append(a)
            return a


if __name__ == '__main__':
    print(len(wordBreak('aaaaaaa', ["aa", "aa", "a"])))
    print(wordBreak('aaaaaaa', ["aa", "aa", "a"]))

    print(len(["a a a a a a a", "aa a a a a a", "a aa a a a a", "a a aa a a a", "aa aa a a a", "aaaa a a a", "a a a aa a a",
     "aa a aa a a", "a aa aa a a", "a aaaa a a", "a a a a aa a", "aa a a aa a", "a aa a aa a", "a a aa aa a",
     "aa aa aa a", "aaaa aa a", "a a aaaa a", "aa aaaa a", "a a a a a aa", "aa a a a aa", "a aa a a aa", "a a aa a aa",
     "aa aa a aa", "aaaa a aa", "a a a aa aa", "aa a aa aa", "a aa aa aa", "a aaaa aa", "a a a aaaa", "aa a aaaa",
     "a aa aaaa"]))
