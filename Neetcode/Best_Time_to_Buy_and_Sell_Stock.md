# Best Time to Buy and Sell Stock

2nd Review: November 4, 2025
Attempts: 2
Date Solved: October 29, 2025
Difficulty: Easy
Status: Solved
Topic/Pattern: Sliding Window

### Link → https://neetcode.io/problems/best-time-to-buy-and-sell-stocks?list=neetcode150

---

## Problem

- You are given an array `prices` where `prices[i]` is the price of a stock on day `i`.
- You are allowed to **buy once and sell once**.
- Return the **maximum profit** you can achieve.
- If no profit is possible, return **0**.

---

### Example

| Input | Output | Reason |
| --- | --- | --- |
| `[7,1,5,3,6,4]` | `5` | Buy at `1`, sell at `6` → `6 - 1 = 5` |
| `[7,6,4,3,1]` | `0` | Prices always decrease → no profit |
| `[1,2]` | `1` | Buy at `1`, sell at `2` |

---

### Approaches

---

### 1. **Brute Force — Try all buy/sell pairs**

```python
def max_profit(prices):
    max_profit = 0

    for i in range(len(prices)):
        for j in range(i+1, len(prices)):
            profit = prices[j] - prices[i]
            max_profit = max(max_profit, profit)

    return max_profit
```

- **Time:** O(n²) — Check every possible buy/sell pair
- **Space:** O(1)
- **Notes:** Very slow when input is large

---

### 2. **Single Pass (Optimal) — Track the lowest buy price**

```python
def max_profit(prices):
    min_price = float('inf')
    max_profit = 0

    for price in prices:
        if price < min_price:
            min_price = price        # Found new lowest buy price
        else:
            profit = price - min_price
            max_profit = max(max_profit, profit)

    return max_profit
```

- **Time:** O(n) — Single loop
- **Space:** O(1) — Constant memory
- **Notes:**
    - Track the **minimum price so far** as the buy day.
    - At each day, calculate profit if selling now.
    - Keep updating max profit.
- **This is the optimal solution.**

---

### Summary

| Approach | Time | Space | Notes |
| --- | --- | --- | --- |
| Brute Force | O(n²) | O(1) | Simple, but too slow |
| Optimal (Single Pass) | O(n) | O(1) | Best approach — efficient and clean |

---

### Edge Cases

| Input | Output | Reason |
| --- | --- | --- |
| `[]` | `0` | No days available |
| `[1]` | `0` | Need at least two days to trade |
| `[9,9,9]` | `0` | No gain possible |
| `[1,100]` | `99` | Huge profit possible |

---

### Tips

- Always think in terms of **"find lowest buying price so far, then sell later"**.
- Never sell before you buy → profit checks must always use prices after the minimum.
- This is a classic **running minimum** pattern.