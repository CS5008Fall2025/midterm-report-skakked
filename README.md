[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/kdfTwECC)
# Midterm p1: Report on Analysis of Fibonacci  Series
* **Author**: Siddharth Kakked
* **GitHub Repo**: https://github.com/CS5008Fall2025/midterm-report-skakked
* **Semester**: Fall 2025
* **Languages Used**: c, python

## Overview

**The Fibonacci Sequence**

> The Fibonacci sequence is a series of numbers where each number is the sum of the two preceding ones. The sequence typically starts with F(0) = 0 and F(1) = 1, resulting in: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144...

> Mathematically it is defined as:
<pre>
F(0) = 0
F(1) = 1
F(n) = F(n-1) + F(n-2) for n ≥ 2
</pre>

> This report analyzes three algorithms (Iterative, Recursive, Dynamic Programming) implemented in two languages (C and Python), resulting in six distinct implementations:

This project explores the time and operation complexity of computing Fibonacci numbers using three classical algorithmic approaches:

1. **Iterative**
2. **Recursive**
3. **Dynamic Programming (DP)** — implemented with memoization in Python and tabulation in C.

Each algorithm was implemented in **C** and **Python**.
The goal is to empirically verify the theoretical Big-O complexity of each method and compare language-level efficiencies. For each algorithm, this report provides: 

1. Big-O analysis with derivation 
2. Pseudocode 
3. Empirical results
4. Language Analysis

---

**Iterative Algorithm**

> The iterative algorithm computes Fibonacci numbers bottom-up, maintaining only the last two values.

Pseudocode:
```
FUNCTION fibonacci_iterative(n):
    IF n ≤ 1:
        RETURN n
    
    a ← 0
    b ← 1
    
    FOR i FROM 2 TO n:
        operations_count++
        temp ← b
        b ← a + b
        a ← temp
    
    RETURN b
END FUNCTION
```
**Big-O Analysis**

**Time Complexity:** `O(n)`
- Executes a single loop from 2 to n.  
- Each iteration performs constant-time operations (one addition, two assignments).  
- `T(n) = c₁ + c₂(n-1)` → `O(n)`.

**Space Complexity:** `O(1)`
- Maintains only two variables (`a`, `b`).  
- No recursion or dynamic structures.  
- `S(n) = O(1)`.

---

**Recursive Algorithm**
> The recursive approach directly implements the mathematical definition of Fibonacci numbers using function calls.
> Each call branches into two more calls, creating an exponential recursion tree with redundancy.

Pseudocode:
```
FUNCTION fibonacci_recursive(n):
    IF n ≤ 1:
        RETURN n
    
    operations_count++
    RETURN fibonacci_recursive(n-1) + fibonacci_recursive(n-2)
END FUNCTION
```
**Big-O Analysis**

**Time Complexity:** `O(2ⁿ)` – Exponential  
Recurrence:
T(n) = T(n-1) + T(n-2) + O(1)
T(0) = T(1) = O(1)


Characteristic Equation:
1. Assume `T(n) = rⁿ`  
2. Substituting: `rⁿ = rⁿ⁻¹ + rⁿ⁻² ⇒ r² = r + 1`  
3. Solving `r = (1 ± √5)/2` 
4. The positive root `φ ≈ 1.618`  

Hence `T(n)= O(φⁿ) ≈ O(1.618ⁿ) ≈ O(2ⁿ)`.


**Space Complexity:** `O(n)`  
- Max recursion depth = n → `S(n)= O(n)`.

---
**Dynamic Programming**
> Dynamic programming adds memoization to recursion, caching computed values to avoid redundant calculations.

Pseudocode:
```
GLOBAL cache ← empty dictionary/array
GLOBAL initialized ← boolean array [false, false, ...]

FUNCTION fibonacci_dp(n):
    IF n ≤ 1:
        RETURN n
    
    IF initialized[n]:
        RETURN cache[n]  // Return cached value
    
    operations_count++
    cache[n] ← fibonacci_dp(n-1) + fibonacci_dp(n-2)
    initialized[n] ← true
    
    RETURN cache[n]
END FUNCTION
```
**Big-O Analysis**

**Time Complexity:** `O(n)`  
- Each Fibonacci value computed once and stored.  
- Lookup = `O(1)`.  
- `T(n) = O(n)`.

**Space Complexity:** `O(n)`  
- Table stores n values.  
- Recursion stack depth = n.  
- `S(n) = O(n)`.

---

## Summary of Complexity Analysis

| **Algorithm** | **Time Complexity** | **Space Complexity** | **Notes** |
|:--------------:|:------------------:|:--------------------:|:-----------|
| **Iterative** | `O(n)` | `O(1)` | Most space-efficient |
| **Recursive** | `O(2ⁿ)` | `O(n)` | Slowest; exponential growth |
| **Dynamic Programming** | `O(n)` | `O(n)` | Fast; uses extra memory |

---

## Empirical Data & Discussion 

**Operations Count Analysis**
> The empirical data validates the theoretical Big-O analysis. Operation counts were measured by incrementing the counter at recursive or loop entry points. The results prove empriically  that algorithmic complexity is language-independent. See tables below and see outputs [ops_c_data.csv](ops_c_data.csv) and [ops_py_data.csv](ops_py_data.csv).

#### C Operations Count
| **N** | **Iterative** | **Dynamic Programming** | **Recursive** |
|-------|---------------:|-------------------------:|---------------:|
| 1     | 0             | 0                       | 1             |
| 2     | 1             | 1                       | 3             |
| 3     | 2             | 2                       | 5             |
| 4     | 3             | 3                       | 9             |
| 5     | 4             | 4                       | 15            |
| 6     | 5             | 5                       | 25            |
| 7     | 6             | 6                       | 41            |
| 8     | 7             | 7                       | 67            |
| 9     | 8             | 8                       | 109           |
| 10    | 9             | 9                       | 177           |
| 11    | 10            | 10                      | 287           |
| 12    | 11            | 11                      | 465           |
| 13    | 12            | 12                      | 753           |
| 14    | 13            | 13                      | 1,219         |
| 15    | 14            | 14                      | 1,973         |
| 16    | 15            | 15                      | 3,193         |
| 17    | 16            | 16                      | 5,167         |
| 18    | 17            | 17                      | 8,361         |
| 19    | 18            | 18                      | 13,529        |
| 20    | 19            | 19                      | 21,891        |
| 21    | 20            | 20                      | 35,421        |
| 22    | 21            | 21                      | 57,313        |
| 23    | 22            | 22                      | 92,735        |
| 24    | 23            | 23                      | 150,049       |
| 25    | 24            | 24                      | 242,785       |
| 26    | 25            | 25                      | 392,835       |
| 27    | 26            | 26                      | 635,621       |
| 28    | 27            | 27                      | 1,028,457     |
| 29    | 28            | 28                      | 1,664,079     |
| 30    | 29            | 29                      | 2,692,537     |
| 31    | 30            | 30                      | 4,356,617     |
| 32    | 31            | 31                      | 7,049,155     |
| 33    | 32            | 32                      | 11,405,773    |
| 34    | 33            | 33                      | 18,454,929    |
| 35    | 34            | 34                      | 29,860,703    |
| 36    | 35            | 35                      | 48,315,633    |
| 37    | 36            | 36                      | 78,176,337    |
| 38    | 37            | 37                      | 126,491,971   |
| 39    | 38            | 38                      | 204,668,309   |
| 40    | 39            | 39                      | 331,160,281   |


#### Python Operations Count 
| **N** | **Iterative** | **Dynamic Programming** | **Recursive** |
|-------|---------------:|-------------------------:|---------------:|
| 1     | 0             | 0                       | 1             |
| 2     | 1             | 1                       | 3             |
| 3     | 2             | 2                       | 5             |
| 4     | 3             | 3                       | 9             |
| 5     | 4             | 4                       | 15            |
| 6     | 5             | 5                       | 25            |
| 7     | 6             | 6                       | 41            |
| 8     | 7             | 7                       | 67            |
| 9     | 8             | 8                       | 109           |
| 10    | 9             | 9                       | 177           |
| 11    | 10            | 10                      | 287           |
| 12    | 11            | 11                      | 465           |
| 13    | 12            | 12                      | 753           |
| 14    | 13            | 13                      | 1,219         |
| 15    | 14            | 14                      | 1,973         |
| 16    | 15            | 15                      | 3,193         |
| 17    | 16            | 16                      | 5,167         |
| 18    | 17            | 17                      | 8,361         |
| 19    | 18            | 18                      | 13,529        |
| 20    | 19            | 19                      | 21,891        |
| 21    | 20            | 20                      | 35,421        |
| 22    | 21            | 21                      | 57,313        |
| 23    | 22            | 22                      | 92,735        |
| 24    | 23            | 23                      | 150,049       |
| 25    | 24            | 24                      | 242,785       |
| 26    | 25            | 25                      | 392,835       |
| 27    | 26            | 26                      | 635,621       |
| 28    | 27            | 27                      | 1,028,457     |
| 29    | 28            | 28                      | 1,664,079     |
| 30    | 29            | 29                      | 2,692,537     |

> Operation counts are identical between C and Python for each algorithm at all tested n values. This definitively proves that Big-O complexity is a property of the algorithm itself, not the implementation language.




## Language Analysis


### Language 1: C



### Language 2: Python



### Comparison and Discussion Between Experiences


## Conclusions / Reflection

## References

