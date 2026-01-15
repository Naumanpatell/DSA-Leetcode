# 3Sum

2nd Review: December 2, 2025
Attempts: 2
Date Solved: October 29, 2025
Difficulty: Medium
Status: Solved
Topic/Pattern: Two Pointers

### Link → https://neetcode.io/problems/3sum?list=neetcode150

---

## Problem

- You are given an integer array `nums`.
- Your task is to return **all unique triplets** `(a, b, c)` in the array such that:

```
a + b + c = 0

```

- Triplets must be returned **without duplicates** (order inside triplet does not matter).

---

### Example

| Input | Output | Reason |
| --- | --- | --- |
| `[-1,0,1,2,-1,-4]` | `[[-1,-1,2],[-1,0,1]]` | Only these pairs sum to zero without repeating |
| `[0,1,1]` | `[]` | No combination adds up to 0 |
| `[0,0,0]` | `[[0,0,0]]` | Triplet of zeros is valid once |

---

### Approaches

---

### 1. **Brute Force — Pick all triplets**

```python
def three_sum(nums):
    result = []
    n = len(nums)

    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                if nums[i] + nums[j] + nums[k] == 0:
                    triplet = sorted([nums[i], nums[j], nums[k]])
                    if triplet not in result:
                        result.append(triplet)
    return result

```

- **Time:** O(n³) — triple nested loops
- **Space:** O(n) — result storage
- **Notes:** Very slow, duplicates are hard to avoid

---

### 2. **Sorting + Two Pointer (Optimal)**

```python
def three_sum(nums):
    nums.sort()
    result = []

    for i in range(len(nums)):
        # Skip duplicate value to avoid duplicate triplets
        if i > 0 and nums[i] == nums[i-1]:
            continue

        left, right = i+1, len(nums)-1

        while left < right:
            s = nums[i] + nums[left] + nums[right]

            if s < 0:
                left += 1
            elif s > 0:
                right -= 1
            else:
                result.append([nums[i], nums[left], nums[right]])
                left += 1
                right -= 1

                # Skip duplicates on left side
                while left < right and nums[left] == nums[left-1]:
                    left += 1

    return result

```

- **Time:** O(n²)
    - Sorting: O(n log n)
    - Two-pointer scanning for each index: O(n²) total
- **Space:** O(1) extra (not counting output)
- **Notes:**
    - Sorting allows duplicate removal easily.
    - Two pointers efficiently find pairs matching `nums[i]`.

---

### Summary

| Approach | Time | Space | Notes |
| --- | --- | --- | --- |
| Brute Force | O(n³) | O(n) | Extremely slow and duplicate-heavy |
| Sorting + Two Pointer | O(n²) | O(1) | Clean, optimal, accepted solution |

---

### Edge Cases

| Input | Output | Reason |
| --- | --- | --- |
| `[]` | `[]` | No elements |
| `[0]` | `[]` | Need 3 numbers |
| `[0,0,0]` | `[[0,0,0]]` | Only one unique triplet |
| `[-2,0,1,1,2]` | `[[-2,0,2],[-2,1,1]]` | Multiple valid pairs |

---

### Tips

- **Always sort first** → makes duplicate removal and pointer logic easy.
- If sum < 0 → move `left` forward (need bigger number).
- If sum > 0 → move `right` backward (need smaller number).
- Skip duplicates for both the **i index** and the **left pointer**.
- This is a classic **Two Pointer after Sorting** pattern.