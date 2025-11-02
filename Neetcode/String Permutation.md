# String Permutation

2nd Review: November 8, 2025
Date Solved: November 2, 2025
Difficulty: Medium
Review: 0
Status: Solved
Topic/Pattern: Sliding Window

### Link → https://neetcode.io/problems/permutation-in-string

## Problem

You are given two strings `s1` and `s2`.

Return **True** if **any permutation** of `s1` exists as a **substring** in `s2`.

Else return **False**.

In other words, check if `s2` contains a substring with **exact same character counts** as `s1`.

---

### Example

| Input | Output | Reason |
| --- | --- | --- |
| `s1 = "ab", s2 = "eidbaooo"` | `True` | `"ba"` is a permutation of `"ab"` |
| `s1 = "ab", s2 = "eidboaoo"` | `False` | No substring with both 'a' and 'b' |
| `s1 = "adc", s2 = "dcda"` | `True` | substring `"cda"` matches letters of `"adc"` |
| `s1 = "a", s2 = "a"` | `True` | exact match |

---

## Approaches

### 1. Brute Force — Generate All Permutations

```python
from itertools import permutations

def checkInclusion(s1, s2):
    for perm in permutations(s1):
        if ''.join(perm) in s2:
            return True
    return False
```

- **Time:** O(n! × n) — generating all permutations is extremely expensive
- **Space:** O(n) — for storing permutations
- **Notes:** Absolutely not usable for large input

---

### 2. Optimal — Sliding Window + Frequency Count (Recommended)

```python
def checkInclusion(s1, s2):
    if len(s1) > len(s2):
        return False

    s1_count = [0] * 26
    s2_count = [0] * 26

    # Count characters of s1 and first window of s2
    for i in range(len(s1)):
        s1_count[ord(s1[i]) - ord('a')] += 1
        s2_count[ord(s2[i]) - ord('a')] += 1

    # Sliding window
    for i in range(len(s2) - len(s1)):
        if s1_count == s2_count:
            return True

        s2_count[ord(s2[i]) - ord('a')] -= 1
        s2_count[ord(s2[i + len(s1)]) - ord('a')] += 1

    return s1_count == s2_count
```

- **Time:** O(n) — each character added & removed once
- **Space:** O(1) — always 26-element lists (constant)
- **Notes:** Classic **Sliding Window + Frequency Array** solution

---

## Summary

| Approach | Time | Space | Notes |
| --- | --- | --- | --- |
| Brute Force | O(n! × n) | O(n) | Too slow, never use |
| Sliding Window + Count Array | **O(n)** | **O(1)** | Best + Optimal |

---

## Edge Cases

| Input | Output | Reason |
| --- | --- | --- |
| `s1=""` | `True` | Empty string is trivially a permutation |
| `len(s1) > len(s2)` | `False` | s2 cannot contain s1 |
| `s1 = "aaa", s2 = "aaaaaa"` | `True` | continuous block matches |
| `s1 = "xyz", s2 = "abcdef"` | `False` | no matching characters |

---

## Tip

- Remember: **Permutation = same character counts**, not order.
- So this problem becomes:
    
    ✔️ Check if **any window** in `s2` has the **same frequency vector** as `s1`.
    
- Whenever comparing **substring by character counts**, think **Sliding Window + Frequency Array**.