"""
 Fibonacci Series Implementation in C
 Name: Siddharth Kakked
 Date: 14th October 2025
 Implements three algorithms for computing Fibonacci numbers:
    1. Iterative 
    2. Recursive 
    3. Dynamic Programming 
"""

from enum import Enum
from functools import lru_cache
import argparse
from typing import Callable
import sys
import time

# Increase recursion limit to handle larger values
sys.setrecursionlimit(100000)

# Global variable to track number of operations
OPS = 0

class FibonacciType(Enum):
    """Enumeration of Fibonacci algorithm types"""
    ITERATIVE_DP_TOGETHER = 4  # Run only iterative and DP for comparison
    ALL = 3                     # Run all three algorithms
    DP = 2                      # Dynamic programming only
    RECURSIVE = 1               # Pure recursion only
    ITERATIVE = 0               # Iterative only

@lru_cache(maxsize=None)
def fibonacci_dp(n: int) -> int:
    """
    Solves fibonacci using Dynamic Programming (recursion with memoization).
    Args:
        n: nth fibonacci number
    Returns:
        nth fibonacci number
    """
    # Base case: first two fibonacci numbers
    if n <= 1:
        return n
    
    # operation counter +1
    global OPS
    OPS += 1
    
    # Recursive call 
    return fibonacci_dp(n - 1) + fibonacci_dp(n - 2)

