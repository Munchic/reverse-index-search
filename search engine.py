from functools import reduce

class SearchEngine():
    def __init__(self, fileName):
        docs = open(fileName, 'r', encoding='utf-8')
        words = {}
        for docNum, line in enumerate(docs.readlines()):
            line = line.split()
            for word in line:
                words[word] = words.get(word, set())
                words[word].add(docNum)
        docs.close()
        self.invIndex = words

    def search(self, query):
        print(reduce(
            lambda a, b: a & b,
            map(
                lambda i: self.invIndex[i],
                query.split())
        ))


engine = SearchEngine('docs.txt')
print(str(engine.invIndex))
engine.search(input())
