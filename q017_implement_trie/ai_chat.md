## 017. 实现 Trie（前缀树）（#208）

- 工具：DSH（Coding Agent，本地 CLI）
- 模型：deepseek-flash
- 日期：2026-11-22
- 分享链接：本地 CLI 无分享链接，故附完整对话记录

### 我的提示词 1

> 我的想法：暴力法的问题在 startsWith 怎么处理？感觉会造成巨大资源浪费。
> 后来改成：节点用 dict。insert 逐字符建节点、末尾标记；search 走到底再看标记；
> startsWith 走到底即可，不看标记。
>
> 卡住：
> 1. 字符集不是 26 个小写字母（比如 Unicode）时，定长数组不行，必须换 dict 吗？
> 2. 为什么一定要 is_end？只靠“节点存在”，插入 apple 后 search("app") 会误判成 true 吗？

### AI 输出摘要 1

1. **Unicode → dict 必须**：26 数组不够、Unicode 数组太占内存，dict 支持任意可哈希 key
2. **is_end 必要**：插入 "apple" 后，`a→p→p` 路径存在，`search("app")` 走完后节点存在但
   不是单词结尾；无 is_end 会误判 true（用表格对比了 4 种查询）
3. 技巧：嵌套 dict 当节点 + `"#"` 作结尾标记，省掉 TreeNode 类（题目只含小写字母，不会冲突）

### 我据此做的修改

- 用嵌套 dict + `"#"` 标记实现，代码压到 20 行
- 本地 15 条用例全过；1 万词插入 + 1 万次查询 20 ms
- 力扣 17/17，40 ms，击败 91.1%，27.61 MB（击败 83.9%）
- thought.md 补「经 AI 提示后的补充」：Unicode 取舍、is_end 必要性表格、`"#"` 技巧、验证
