/*
 * Fibonacci Series Implementation in C
 * Name: Siddharth Kakked
 * Date: 14th October 2025
 * Implements three algorithms for computing Fibonacci numbers:
 * 1. Iterative 
 * 2. Recursive 
 * 3. Dynamic Programming 
 * 
 */
#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#include <time.h>
#include <stdint.h>

// Max size for the table
#define MAX 50010

// To handle large numbers
typedef uint64_t ull;

// Memoization table for DP algorithm
static ull table[MAX];
// Track values already computed
static bool initialized[MAX] = {false};

/**
 * Prints the fibonacci series to stdout
 * 
 * @param series - array of numbers
 * @param size - # of elements to print
 */
void printSeries(ull *series, int size)
{
    for (int i = 0; i < size; i++)
    {
        printf("%llu ", series[i]);
    }
    printf("\n");
}

/**
 * Computes the nth Fibonacci number using dynamic programming 
 * Using memoization.
 * 
 * @param n - nth fibonacci number
 * @param ops -operation counter 
 * @return nth fibonacci number
 */
ull fibonacci_dp(int n, ull *ops)
{
    // Base case: F(0) = 0, F(1) = 1
    if (n <= 1)
    {
        return n;
    }
    
    // Check if value already computed 
    // Memoization lookup
    if (initialized[n])
    {
        return table[n];
    }
    
    // Operation Counter +1
    (*ops)++;
    
    // Recursive Call
    table[n] = fibonacci_dp(n - 1, ops) + fibonacci_dp(n - 2, ops);
    initialized[n] = true;
    
    return table[n];
}

/**
 * Generates the complete Fibonacci series
 * 
 * @param n - generate series up to the nth fibonacci number
 * @param ops - pointer to operation counter
 * @return pointer to array 
 */
ull *fibonacci_dp_full(int n, ull *ops)
{
    // Allocate memory
    ull *series = malloc(sizeof(ull) * n);
    
    // Generates numbers
    for (int i = 1; i <= n; i++)
    {
        series[i - 1] = fibonacci_dp(i, ops);
    }
    
    return series;
}
/**
 * Recursion (no dynamic programming).
 * 
 * @param n - nth fibonacci number
 * @param ops - operation counter
 * @return nth fibonacci number
 */
ull fibonacci_r(int n, ull *ops)
{
    // Base case: F(0) = 0, F(1) = 1
    if (n <= 1)
    {
        return n;
    }

    // Operation Counter +1
    (*ops)++;
    
    // Recursive calls
    return fibonacci_r(n - 1, ops) + fibonacci_r(n - 2, ops);
}

/**
 * Generates the complete Fibonacci series from F(1) to F(n)
 * 
 * 
 * @param n - generate series up to the nth fibonacci number
 * @param ops - pointer to operation counter
 * @return pointer to array
 */
ull *fibonacci_r_full(int n, ull *ops)
{
    // Allocate memory
    ull *series = malloc(sizeof(ull) * n);
    
    // Generate sequence
    for (int i = 1; i <= n; i++)
    {
        series[i - 1] = fibonacci_r(i, ops);
    }
    
    return series;
}

