# 017. 208. 实现 Trie (前缀树)

- LeetCode: https://leetcode.cn/problems/implement-trie-prefix-tree/
- 分类: 设计
- 开始时间: ____-__-__ __:__
- 用时: ____ 分钟

## 我的第一想法（未使用 AI）

1. 暴力法，初始化和void直接处理，boolean直接检索。问题在于boolean startsWith(String prefix)如何处理？也是暴力法吗？（不可行，会造成巨大的资源浪费）
2. 节点使用dict.insert：从根往下逐字符走，缺子节点就新建，走完把最后一个节点标记为结尾.search：逐字符往下走，中途缺节点返回 false；走到底还要看结尾标记，否则 apple 的前缀 app 会被误判成单词.startsWith：和 search 一样走到底，但只看“路径存在”，不看结尾标记。

## 复杂度

- 时间：O(L)
- 空间：O(总字符数)

## 边界情况

- 
- - insert("apple") 后 search("apple") → true
- insert("apple") 后 search("app") → false
- insert("apple") 后 startsWith("app") → true
- insert("apple")、insert("app") 后 search 两者都 → true
- insert("a") 后 search("a") → true、startsWith("a") → true
- 重复插入同一个单词 → 再查仍为 true

## 卡住的地方 / 想向 AI 验证的点

- 
