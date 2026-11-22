"""011. 最长回文子串（#5）

思路见 thought.md：动态规划（按长度递增填表）。
另有中心扩展版作对照（空间 O(1)）。
"""

from typing import List


class Solution:
    def longestPalindrome(self, s: str) -> str:
        """DP：dp[i][j] 表示 s[i..j] 是否回文。时间 O(n²)，空间 O(n²)。"""
        n = len(s)
        if n < 2:
            return s

        dp = [[False] * n for _ in range(n)]
        start, max_len = 0, 1

        for i in range(n):
            dp[i][i] = True

        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                if s[i] == s[j]:
                    if length <= 3:
                        dp[i][j] = True
                    else:
                        dp[i][j] = dp[i + 1][j - 1]
                if dp[i][j] and length > max_len:
                    max_len = length
                    start = i

        return s[start:start + max_len]

    def longestPalindromeExpand(self, s: str) -> str:
        """中心扩展：2n-1 个中心。时间 O(n²)，空间 O(1)。"""
        if not s:
            return ""

        def expand(l: int, r: int) -> int:
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            return r - l - 1

        best_start, best_len = 0, 1
        for i in range(len(s)):
            o = expand(i, i)          # 奇数长度
            e = expand(i, i + 1)      # 偶数长度
            cur = max(o, e)
            if cur > best_len:
                best_len = cur
                best_start = i - (cur - 1) // 2
        return s[best_start:best_start + best_len]


def brute(s: str) -> str:
    """O(n³) 暴力，仅用于对拍。"""
    best = ""
    for i in range(len(s)):
        for j in range(i, len(s)):
            t = s[i:j + 1]
            if t == t[::-1] and len(t) > len(best):
                best = t
    return best


if __name__ == "__main__":
    cases = [
        ("", ""),
        ("a", "a"),
        ("aa", "aa"),
        ("ab", "a"),
        ("aba", "aba"),
        ("abba", "abba"),
        ("abb", "bb"),
        ("cbbd", "bb"),
        ("babad", "bab"),
        ("aaaa", "aaaa"),
        ("abcba", "abcba"),
        ("ac", "a"),
    ]

    print("=== 固定用例（DP / 中心扩展）===")
    ok_dp = ok_ex = 0
    for s, want in cases:
        a = Solution().longestPalindrome(s)
        b = Solution().longestPalindromeExpand(s)
        # babad 的 "bab" 与 "aba" 都合法，这里只校验长度一致
        good_dp = a == want or (s == "babad" and a in ("bab", "aba"))
        good_ex = b == want or (s == "babad" and b in ("bab", "aba"))
        ok_dp += good_dp
        ok_ex += good_ex
        print(f"[DP {'PASS' if good_dp else 'FAIL'}] [扩展 {'PASS' if good_ex else 'FAIL'}] "
              f"{s!r:<10} -> {a!r:<8} / {b!r:<8} (want {want!r})")
    print(f"DP {ok_dp}/{len(cases)}   中心扩展 {ok_ex}/{len(cases)}")

    print("\n=== 随机对拍（长度<=10，200 组）===")
    import random
    import string
    random.seed(7)
    bad = 0
    for _ in range(200):
        s = "".join(random.choice("abc") for _ in range(random.randint(0, 10)))
        ref = len(brute(s))
        a = Solution().longestPalindrome(s)
        b = Solution().longestPalindromeExpand(s)
        if len(a) != ref or len(b) != ref or a != a[::-1] or b != b[::-1]:
            bad += 1
            print(f"  FAIL {s!r} dp={a!r} ex={b!r} ref={brute(s)!r}")
    print(f"对拍通过 {200 - bad}/200")
