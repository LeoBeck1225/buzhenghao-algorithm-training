## 005. 无重复字符的最长子串（#3）

- 工具：DSH（Coding Agent，本地 CLI）
- 模型：deepseek-flash
- 日期：2026-11-22
- 分享链接：本地 CLI 无分享链接，故附完整对话记录

### 我的提示词 1

> 这题之前练过：双指针 + 字典 last 记录每个字符上次出现的下标，
> r 不断右扩，遇到重复就把 l 跳到 last[c]+1；last[c] 小于 l 说明在窗口外，不用重复缩。
> 我把代码贴进了 solution.py 模板里，帮我看看对不对。

### AI 输出摘要 1

- 算法本身正确，`last[c] >= l` 的判断是关键（没有它 `"abba"` 会算成 3）
- 但文件有两个问题：
  1. `raise NotImplementedError` 没删，且它在代码前面 → 后面的代码全是死代码
  2. 函数名还是模板的 `def solve(self)`，LeetCode 要 `lengthOfLongestSubstring(self, s)`
- 建议补本地自测用例：`""`、`"a"`、`"aa"`、`"abba"`、`"abcabcbb"`、`"pwwkew"`、`"dvdf"`、`"bbbbb"`

### 我据此做的修改

- 删掉 `raise NotImplementedError`，函数名改为 `lengthOfLongestSubstring`
- 补 8 条本地测试，全部 PASS；10 万字符压测 13 ms
- 力扣 1036/1036，266 ms，击败 92.8%
