"""018. LRU 缓存（#146）

思路见 thought.md：哈希表（key → 节点）+ 双向链表（维护访问顺序）。
头部 = 最近使用，尾部 = 最久未使用；两个哨兵省掉空链表特判。
get / put 均 O(1)，空间 O(capacity)。
"""


class _Node:
    __slots__ = ("key", "value", "prev", "next")

    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache(object):

    def __init__(self, capacity):
        self.cap = capacity
        self.cache = {}
        self.head = _Node()
        self.tail = _Node()
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def _add_front(self, node):
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

    def get(self, key):
        node = self.cache.get(key)
        if node is None:
            return -1
        self._remove(node)
        self._add_front(node)
        return node.value

    def put(self, key, value):
        node = self.cache.get(key)

        if node is not None:
            node.value = value
            self._remove(node)
            self._add_front(node)
            return

        if len(self.cache) >= self.cap:
            victim = self.tail.prev
            self._remove(victim)
            del self.cache[victim.key]

        node = _Node(key, value)
        self.cache[key] = node
        self._add_front(node)

    # 调试用：按链表顺序返回 key
    def _keys(self):
        out, cur = [], self.head.next
        while cur is not self.tail:
            out.append(cur.key)
            cur = cur.next
        return out


if __name__ == "__main__":
    # 官方示例
    c = LRUCache(2)
    c.put(1, 1); c.put(2, 2)
    r1 = c.get(1)
    c.put(3, 3)
    r2 = c.get(2)
    c.put(4, 4)
    r3 = c.get(1)
    r4 = c.get(3)
    r5 = c.get(4)
    exp = [1, -1, -1, 3, 4]
    got = [r1, r2, r3, r4, r5]
    print(f"[{'PASS' if got == exp else 'FAIL'}] 官方示例 {got} (want {exp})")

    # 容量 1
    c1 = LRUCache(1)
    c1.put(1, 1); c1.put(2, 2)
    ok1 = c1.get(1) == -1 and c1.get(2) == 2
    print(f"[{'PASS' if ok1 else 'FAIL'}] 容量1")

    # 更新不算新增
    c2 = LRUCache(2)
    c2.put(1, 1); c2.put(2, 2)
    c2.put(1, 10)
    ok2 = c2.get(1) == 10 and c2.get(2) == 2
    print(f"[{'PASS' if ok2 else 'FAIL'}] 更新已有 key 不淘汰")

    # get 提升优先级
    c3 = LRUCache(2)
    c3.put(1, 1); c3.put(2, 2)
    c3.get(1)
    c3.put(3, 3)
    ok3 = c3.get(1) == 1 and c3.get(2) == -1
    print(f"[{'PASS' if ok3 else 'FAIL'}] get 提升优先级 -> 链表 {c3._keys()}")

    # 不变量：链表节点数 == cache 大小
    c4 = LRUCache(3)
    for i in range(10):
        c4.put(i, i)
    ok4 = len(c4._keys()) == len(c4.cache) == 3
    print(f"[{'PASS' if ok4 else 'FAIL'}] 不变量: 链表 {len(c4._keys())} 个, cache {len(c4.cache)} 个")

    # 性能
    import time
    t = time.time()
    c5 = LRUCache(1000)
    for i in range(50000):
        c5.put(i, i)
    for i in range(50000):
        c5.get(i)
    print(f"[性能] 10 万次操作 {(time.time() - t) * 1000:.0f} ms")
