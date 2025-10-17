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

**Recursive Algorithm**
> The recursive approach directly implements the mathematical definition of Fibonacci numbers using function calls.
> Each call branches into two more calls, creating an exponential recursion tree with redundancy.

Pseudocode:
```
FUNCTION fibonacci_recursive(n):
IF n ≤ 1:
RETURN n
RETURN fibonacci_recursive(n-1) + fibonacci_recursive(n-2)
```
**Big-O Analysis**

**Time Complexity:** `O(2ⁿ)` – Exponential  

Recurrence:
T(n) = T(n-1) + T(n-2) + O(1)
T(0) = T(1) = O(1)

markdown
Copy code

Characteristic Equation:
1. `T(n)=rⁿ`  
2. `rⁿ = rⁿ⁻¹ + rⁿ⁻² ⇒ r² = r + 1`  
3. `r = (1 ± √5)/2 ⇒ φ ≈ 1.618`  

Hence `T(n)=O(φⁿ)≈O(1.618ⁿ)≈O(2ⁿ)`.

**Recursion Tree Example**
fib(5)
├─ fib(4)
│ ├─ fib(3)
│ └─ fib(2)
└─ fib(3)
├─ fib(2)
└─ fib(1)

markdown
Copy code
- Height ≈ n  
- Total nodes ≈ `2⁰ + 2¹ + … + 2ⁿ ≈ 2ⁿ⁺¹−1`  
→ `T(n)=O(2ⁿ)`

**Space Complexity:** `O(n)`  
- Max recursion depth = n → `S(n)=O(n)`.

---








## Empirical Data & Discussion 


## Language Analysis


### Language 1: C



### Language 2: UPDATE



### Comparison and Discussion Between Experiences


## Conclusions / Reflection

## References

