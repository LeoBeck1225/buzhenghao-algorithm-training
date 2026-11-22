# 018. LRU 缓存（#146）

- LeetCode: https://leetcode.cn/problems/lru-cache/
- 分类: 设计
- 开始时间: 2026-11-22 14:40
- 用时: 约 50 分钟

## 我的第一想法（未使用 AI，原文保留）

1. 先把get()和put()拆开看，使用哈希表负责查找。双向链表负责维护“最近使用顺序”。我想要采用字典结构。节点存 key、value、prev、next 四个字段
2. 用双向是因为删除任意节点要同时改前驱和后继

## 复杂度

- 时间：O(1)
- 空间：O(capacity)

## 边界情况

- capacity = 1，put(1,1)、put(2,2) 后 get(1) → -1，get(2) → 2
- get 不存在的 key → -1
- put 已存在的 key 更新值 → get 返回新值，容量不变
- 更新已有 key 后它成为最近使用，淘汰时不会先被淘汰
- get 某 key 后该 key 成为最近使用，淘汰的是别的 key
- put 时容量刚好满 → 插入新键后再淘汰尾部
- 容量满且 put 已存在的 key → 不淘汰任何键

## 卡住的地方 / 想向 AI 验证的点

- 难度真的有点大。有点卡住了
- 这一题我用了很多 AI 的提示，因为实在想不出来

## 经 AI 提示后的补充（这部分不是原话，单独记录）

### ① 为什么节点要存 key

淘汰的是链表尾节点，但**哈希表也要同步删掉**：

```python
victim = self.tail.prev
self._remove(victim)
del self.cache[victim.key]     # ← 没有 key 字段就做不到
```

这就是四个字段里 `key` 的存在意义（节点只存 value 的话，淘汰时会留下幽灵 key）。

### ② 为什么要两个哨兵

```
head <-> n1 <-> n2 <-> ... <-> tail
```

- `head.next` 永远是**最近使用**
- `tail.prev` 永远是**最久未使用**

有了哨兵，`_remove` / `_add_front` 永远不需要判空（不会遇到"链表只有一个元素"这种特判）。

### ③ 两个积木 + 四个动作

两个积木：

```python
def _remove(self, node):        # 从链表摘下（不动 dict）
def _add_front(self, node):     # 插到 head 之后 = 标记最近使用
```

四个动作：

| 操作 | 组合 |
|---|---|
| `get` 命中 | `_remove` → `_add_front` → 返回 value |
| `get` 未命中 | 返回 -1 |
| `put` 已存在 | 改 value → `_remove` → `_add_front`（**不淘汰**） |
| `put` 不存在 | 满了就 `_remove(tail.prev)` + `del cache[key]`；再新建 + `_add_front` |

### ④ 为什么必须双向链表

删任意节点要同时改**前驱和后继**。单链表只能 O(n) 找前驱，双向链表自带 `prev` → O(1)。

### ⑤ 三个高频错误

1. 淘汰时忘了 `del self.cache[victim.key]` → 幽灵节点，`get` 返回已淘汰的值
2. `put` 已存在的 key 当成新增 → 触发淘汰，容量白丢
3. `_add_front` 里先改 `self.head.next = node` → 丢失旧节点，链表断裂

### ⑥ 验证

- 官方示例、容量 1、更新不淘汰、get 提升优先级、链表/字典数量不变量：全部通过
- 10 万次 put + get：30 ms
- 力扣：23/23，65 ms，击败 42.6%，22.55 MB（击败 79.8%）
