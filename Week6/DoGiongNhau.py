class Node:
    def __init__(self) -> None:
        self.countWord = 0
        self.child = dict()


class Trie:
    def __init__(self) -> None:
        self.root = Node()

    def addWord(self, word: str) -> None:
        temp = self.root
        for character in word:
            if character not in temp.child:
                temp.child[character] = Node()
            temp = temp.child[character]
        temp.countWord += 1

    def searchWord(self, word: str) -> int:
        temp = self.root
        for character in word:
            if character not in temp.child:
                return 0
            temp = temp.child[character]
        return temp.countWord 


def solve() -> None:
    a = input().strip()
    b = input().strip()

    if len(a) == 1 or len(b) == 1:
        print(0)

    trie = Trie()

    for i in range(1, len(a)):
        trie.addWord(a[i-1]+a[i])

    ans = 0
    for i in range(1, len(b)):
        ans += trie.searchWord(b[i-1]+b[i])

    print(ans)


solve()
