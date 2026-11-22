# 017. 实现 Trie（前缀树）（#208）

- LeetCode: https://leetcode.cn/problems/implement-trie-prefix-tree/
- 分类: 设计
- 开始时间: 2026-11-22 14:15
- 用时: 约 20 分钟

## 我的第一想法（未使用 AI，原文保留）

1. 暴力法，初始化和void直接处理，boolean直接检索。问题在于boolean startsWith(String prefix)如何处理？也是暴力法吗？（不可行，会造成巨大的资源浪费）
2. 节点使用dict。insert：从根往下逐字符走，缺子节点就新建，走完把最后一个节点标记为结尾。search：逐字符往下走，中途缺节点返回 false；走到底还要看结尾标记，否则 apple 的前缀 app 会被误判成单词。startsWith：和 search 一样走到底，但只看“路径存在”，不看结尾标记。

## 复杂度

- 时间：O(L)
- 空间：O(总字符数)

## 边界情况

- insert("apple") 后 search("apple") → true
- insert("apple") 后 search("app") → false
- insert("apple") 后 startsWith("app") → true
- insert("apple")、insert("app") 后 search 两者都 → true
- insert("a") 后 search("a") → true、startsWith("a") → true
- 重复插入同一个单词 → 再查仍为 true

## 卡住的地方 / 想向 AI 验证的点

- 如果字符集不是 26 个小写字母（比如 Unicode），定长数组就不行，必须换 dict 吗？
- 为什么一定要 is_end 标记？只靠“节点存在”判断，插入 apple 后 search("app") 会不会被误判成 true

## 经 AI 提示后的补充（这部分不是原话，单独记录）

### ① Unicode 场景：dict 是必须的

- 26 定长数组只够 a-z
- 按 Unicode 开数组（65536 格）→ 每个节点都极占内存
- `dict` 支持任意可哈希 key，是**字符集不确定时的正确选择**

### ② 为什么必须 is_end

插入 "apple" 后，路径 `a → p → p → l → e` 存在，`"app"` 也走这条路径：

| 查询 | 走到 | 节点存在 | 是单词结尾 | 无 is_end 结果 | 正确 |
|---|---|---|---|---|---|
| search("apple") | e | ✅ | ✅ | true | true |
| search("app") | 第 2 个 p | ✅ | ❌ | **true（错）** | false |
| search("appl") | l | ✅ | ❌ | **true（错）** | false |
| startsWith("app") | 第 2 个 p | ✅ | 不看 | true | true |

没有 `is_end`，`search` 就退化成 `startsWith`。

### ③ 实现技巧：嵌套字典 + "#" 标记

不写 TreeNode 类，直接把 `dict` 当节点：

```python
def insert(self, word):
    node = self.root
    for ch in word:
        node = node.setdefault(ch, {})
    node["#"] = True            # "#" 作为结尾标记
```

- 为什么用 `"#"` 安全：题目保证单词只含小写字母，不会与 `"#"` 冲突
- 好处：代码短、不用额外类；代价：可读性略低于 `TrieNode` 类

### ④ 验证

- 15 条用例全过（含空串行为：`search("") = False`、`startsWith("") = True`）
- 1 万词插入 + 5000 次 search + 5000 次 startsWith：**20 ms**
- 力扣：17/17，40 ms，击败 91.1%，27.61 MB（击败 83.9%）
