"""017. 实现 Trie（前缀树）（#208）

思路见 thought.md：嵌套字典当节点，用 "#" 作为“单词结尾”标记。
  - insert：逐字符 setdefault 建节点，末尾 node["#"] = True
  - search：走完字符后看 "#" 是否存在
  - startsWith：走完字符即可，不看 "#"
时间 O(L) / 次操作，空间 O(总字符数)。
"""

import random
import string
import time


class Trie:
    def __init__(self):
        self.root = {}

    def insert(self, word):
        node = self.root
        for ch in word:
            node = node.setdefault(ch, {})
        node["#"] = True

    def search(self, word):
        node = self.root
        for ch in word:
            if ch not in node:
                return False
            node = node[ch]
        return "#" in node

    def startsWith(self, prefix):
        node = self.root
        for ch in prefix:
            if ch not in node:
                return False
            node = node[ch]
        return True


if __name__ == "__main__":
    checks = []

    # LeetCode 官方示例
    t = Trie()
    t.insert("apple")
    checks += [
        ("search apple", t.search("apple"), True),
        ("search app", t.search("app"), False),
        ("startsWith app", t.startsWith("app"), True),
    ]
    t.insert("app")
    checks += [
        ("search app after insert", t.search("app"), True),
    ]

    # 边界与链式前缀
    t2 = Trie()
    t2.insert("a")
    checks += [
        ("search a", t2.search("a"), True),
        ("search ab", t2.search("ab"), False),
        ("startsWith a", t2.startsWith("a"), True),
    ]

    t3 = Trie()
    for w in ("ab", "abc", "abcd"):
        t3.insert(w)
    checks += [
        ("search ab", t3.search("ab"), True),
        ("search abc", t3.search("abc"), True),
        ("search abcd", t3.search("abcd"), True),
        ("search abcde", t3.search("abcde"), False),
        ("startsWith abc", t3.startsWith("abc"), True),
    ]

    # 重复插入
    t4 = Trie()
    t4.insert("word")
    t4.insert("word")
    checks += [("repeat insert then search", t4.search("word"), True)]

    # 空串行为（题目保证非空，仅作观察）
    t5 = Trie()
    t5.insert("x")
    checks += [
        ("search '' ", t5.search(""), False),
        ("startsWith '' ", t5.startsWith(""), True),
    ]

    ok = 0
    for name, got, want in checks:
        passed = got == want
        ok += passed
        print(f"[{'PASS' if passed else 'FAIL'}] {name:<28} -> {got} (want {want})")
    print(f"\n{ok}/{len(checks)} passed")

    # 性能：1 万个词
    random.seed(1)
    words = ["".join(random.choice(string.ascii_lowercase) for _ in range(random.randint(3, 12)))
             for _ in range(10000)]
    t = Trie()
    start = time.time()
    for w in words:
        t.insert(w)
    for w in words[:5000]:
        t.search(w)
    for w in words[:5000]:
        t.startsWith(w[:3])
    print(f"\n1 万词插入 + 5000 次 search + 5000 次 startsWith：{(time.time() - start) * 1000:.0f} ms")
