"""007. 删除链表的倒数第 N 个结点（#19）

思路见 thought.md：哑节点 + 快慢指针，两者相差 n 个节点。
时间 O(L)，空间 O(1)（L 为链表长度）。
"""

from typing import Optional


class ListNode:
    def __init__(self, val: int = 0, next: "Optional[ListNode]" = None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        fast = slow = dummy
        for _ in range(n):
            fast = fast.next
        while fast.next:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        return dummy.next


def build(vals):
    dummy = ListNode(0)
    cur = dummy
    for v in vals:
        cur.next = ListNode(v)
        cur = cur.next
    return dummy.next


def to_list(head):
    out = []
    while head:
        out.append(head.val)
        head = head.next
    return out


if __name__ == "__main__":
    cases = [
        ([1, 2, 3, 4, 5], 2, [1, 2, 3, 5]),
        ([1], 1, []),
        ([1, 2], 2, [2]),
        ([1, 2], 1, [1]),
        ([1, 2, 3], 2, [1, 3]),
        ([1, 2, 3], 3, [2, 3]),
    ]

    ok = 0
    for vals, n, want in cases:
        got = to_list(Solution().removeNthFromEnd(build(vals), n))
        passed = got == want
        ok += passed
        flag = "PASS" if passed else "FAIL"
        print(f"[{flag}] {str(vals):<16} n={n} -> {got} (want {want})")
    print(f"\n{ok}/{len(cases)} passed")
