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

def fibonacci_r(n: int) -> int:
    """
    Solves fibonacci usinge recursion (No dynamic programming).
    This demonstrates exponential time complexity.
    
    Args:
        n (int): nth fibonacci number (0-indexed)

    Returns:
         nth fibonacci number
    """
    # Base case
    if n <= 1:
        return n
    
    # operation counter +1
    global OPS
    OPS += 1
    
    # Recursive call
    return fibonacci_r(n - 1) + fibonacci_r(n - 2)

def fibonacci_series_recursive(n: int, func) -> list:
    """
    Calls the provided recursive function for each value from 1 to n.
    
    Args:
        n:  nth fibonacci number
        func: function to use (recursive or dp)

    Returns:
        list of fibonacci numbers from F(1) to F(n)
    """
    result = []
    # Generate each fibonacci number in sequence
    for i in range(1, n + 1):
        result.append(func(i))
    return result

def fibonacci_iterative(n: int) -> int:
    """
    Generates the nth fibonacci number iteratively.
    
    Args:
        n: the fibonacci number to generate

    Returns:
        the nth fibonacci number
    """
    global OPS
    
    # Base case
    if n <= 1:
        return n
    
    # Initialize first two fibonacci numbers
    a, b = 0, 1
    
    # Iteratively compute each fibonacci number
    for i in range(2, n + 1):
        OPS += 1  # Count each addition operation
        a, b = b, a + b  # Shift window forward
    
    return b

def fibonacci_series_iterative(n: int) -> list:
    """
    Generates fibonacci series from 1 to n iteratively.
    
    Args:
        n: the nth fibonacci number

    Returns:
        list of fibonacci numbers from F(1) to F(n)
    """
    global OPS
    result = []
    
    # Handle first fibonacci number: F(1) = 1
    if n >= 1:
        result.append(1)
    
    # Handle second fibonacci number: F(2) = 1
    if n >= 2:
        result.append(1)
    
    # Generate remaining fibonacci numbers
    for i in range(3, n + 1):
        OPS += 1  # Count each addition operation
        # Each number is sum of previous two
        result.append(result[-1] + result[-2])
    
    return result

def fibonacci_dp_full(n: int) -> list:
    """
    Generates fibonacci series from 1 to n using dynamic programming.
    Args:
        n: nth fibonacci number

    Returns:
        list of fibonacci numbers from F(1) to F(n)
    """
    return fibonacci_series_recursive(n, func=fibonacci_dp)

def fibonacci_r_full(n: int) -> list:
    """
    Generates fibonacci series from 1 to n using pure recursion.
    Wrapper function that uses the non-memoized recursive approach.
    WARNING: Very slow for large n due to exponential time complexity.
    
    Args:
        n (int): the nth fibonacci number

    Returns:
        list of fibonacci numbers from F(1) to F(n)
    """
    return fibonacci_series_recursive(n, func=fibonacci_r)


def run_and_time(func: Callable, n: int, print_it: bool = False):
    """
    Runs the fibonacci generation function and measures execution time and operations.
    
    Args:
        func: function to run
        n (int): the nth fibonacci number
        print_it (bool): whether to print the result

    Returns:
        tuple: (execution_time, operations_count)
    """
    global OPS
    OPS = 0  # Reset operation counter
    
    # Measure execution time using high-resolution timer
    start = time.perf_counter()
    result = func(n)
    end = time.perf_counter()
    
    # Optionally print the generated series
    if print_it:
        print(result)
    
    return end - start, OPS

def main(n: int, algo: FibonacciType, print_it: bool):
    """
    Main execution function that runs the specified algorithm(s).

    Args:
        n: nth fibonacci number to generate
        algo: algorithm type to use
        print_it: whether to print the fibonacci series
    """
    if algo == FibonacciType.RECURSIVE:
        # Run only recursive algorithm
        print("Recursive Version")
        time_val, ops = run_and_time(fibonacci_r_full, n, print_it)
        print(f"Time: {time_val}({ops})")
        
    elif algo == FibonacciType.DP:
        # Run only dynamic programming algorithm
        print("Dynamic Programming Version")
        time_val, ops = run_and_time(fibonacci_dp_full, n, print_it)
        print(f"Time: {time_val}({ops})")
        
    elif algo == FibonacciType.ITERATIVE_DP_TOGETHER:
        # Run iterative and DP for comparison (skip slow recursive)
        time_val, ops = run_and_time(fibonacci_series_iterative, n)
        time2, ops2 = run_and_time(fibonacci_dp_full, n)
        # CSV format: time1,ops1,time2,ops2,-,- (placeholders for recursive)
        print(f"{time_val:0.6f},{ops},{time2:0.6f},{ops2},-,-")
        
    elif algo == FibonacciType.ALL:
        # Run all three algorithms for complete comparison
        time_val, ops = run_and_time(fibonacci_series_iterative, n)
        time2, ops2 = run_and_time(fibonacci_dp_full, n)
        time3, ops3 = run_and_time(fibonacci_r_full, n)
        # CSV format: time1,ops1,time2,ops2,time3,ops3
        print(f"{time_val:0.6f},{ops},{time2:0.6f},{ops2},{time3:0.6f},{ops3}")
        
    else:
        # Default: run only iterative algorithm
        print("Iterative Version")
        time_val, ops = run_and_time(fibonacci_series_iterative, n, print_it)
        print(f"Time: {time_val}({ops})")


if __name__ == "__main__":
    # Set up command line argument parsing
    parser = argparse.ArgumentParser(description="Fibonacci Series")
    parser.add_argument("n", type=int, help="The nth fibonacci number to generate")
    parser.add_argument(
        "--print", action="store_true", default=False, help="Print the fibonacci series"
    )
    parser.add_argument(
        "algo",
        type=int,
        choices=[0, 1, 2, 3, 4],
        default=FibonacciType.ITERATIVE.value,
        help="The type of algorithm to use: 0 = iterative, 1 = recursive, 2 = dp, 3 = all, 4 = iterative and dp together",
    )

    # Parse arguments and run
    args = parser.parse_args()
    algo = FibonacciType(args.algo)
    main(args.n, algo, args.print)
