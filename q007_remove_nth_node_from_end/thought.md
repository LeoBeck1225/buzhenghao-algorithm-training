# 007. 删除链表的倒数第 N 个结点（#19）

- LeetCode: https://leetcode.cn/problems/remove-nth-node-from-end-of-list/
- 分类: 链表
- 开始时间: 2026-11-22 10:15
- 用时: 约 20 分钟

## 我的第一想法（未使用 AI，原文保留）

1. 使用一前一后双指针，前后指针相差N，这样当后指针走到尾节点上时前指针恰好在被删掉的结点前一个
2. 采用while遍历，条件为后指针的next。前后指针间隔相差N

## 复杂度

- 时间：O(n)
- 空间：O(1)

## 边界情况

- `[1], n=1` → `[]`（删唯一节点）
- `[1,2], n=2` → `[2]`（删头）
- `[1,2], n=1` → `[1]`（删尾）
- `[1,2,3], n=2` → `[1,3]`（删中间）

## 卡住的地方 / 想向 AI 验证的点

- 要不要使用哑节点dummy？前指针该放在dummy吗？要删除头节点该怎么做？

## 经 AI 提示后的补充（这部分不是原话，单独记录）

### ① 为什么要用哑节点

删除**头节点**时，慢指针需要停在"头的前一个"，而头节点没有前一个 →
用 `dummy` 提供一个虚拟前驱，让"删头"和"删其他节点"走同一套逻辑，不需要特判。

### ② 指针初始化与移动

```
dummy = ListNode(0, head)
slow = fast = dummy
fast 先走 n 步              # 此时 slow 与 fast 相差 n 个节点
while fast.next:            # 同步前进，直到 fast 到尾节点
    fast = fast.next
    slow = slow.next
slow.next = slow.next.next  # slow 正好停在待删节点的前一个
return dummy.next
```

### ③ 走查（`1→2→3→4→5`，n=2，删 4）

| 步骤 | slow | fast |
|---|---|---|
| 初始 | dummy | dummy |
| fast 走 2 步 | dummy | 2 |
| 同步走 1 | 1 | 3 |
| 同步走 2 | 2 | 4 |
| 同步走 3 | 3 | 5（尾节点，停） |
| 删除 | `slow.next = 4` 被跳过 | — |

### ④ 为什么删头也能处理

`1→2`、n=2：fast 走 2 步直接到 None，`while fast.next` 不执行，slow 仍在 dummy，
执行 `slow.next = slow.next.next` 即 `dummy.next = 2`，头节点被删。

### ⑤ 两种写法的区别

- `fast` 先走 **n** 步 + `while fast.next`：结束时 slow 停在**待删节点前** ✅（本解法）
- 若把条件写成 `while fast`：会差一步，slow 停在待删节点本身，需要额外处理

### ⑥ 复杂度依据

- 时间 O(L)：fast 先走 n 步，再同步走 L-n 步，合计 O(L)
- 空间 O(1)：只用了两个指针和一个 dummy
