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
/**
 * Iteratively computes the Fibonacci series.
 * 
 * @param n - generate series 
 * @param ops - operation counter
 * @return pointer to array 
 */
ull *fibonacci_iterative(int n, ull *ops)
{
    // Allocate memory 
    ull *series = malloc(sizeof(ull) * n);
    
    // Initialize first fibonacci number: F(1) = 1
    if (n >= 1)
    {
        series[0] = 1;
    }
    
    // Initialize second fibonacci number: F(2) = 1
    if (n >= 2)
    {
        series[1] = 1;
    }
    
    // Remaining series
    for (int i = 2; i < n; i++)
    {
        (*ops)++;  // Count each addition operation
        series[i] = series[i - 1] + series[i - 2];
    }
    
    return series;
}
/**
 * Times the execution of a fibonacci function
 * Uses clock() for cross-platform compatibility (Windows and Unix).
 * Code adapted from: Dynamic Programming Lab/ Class Code
 */
double time_function(ull *(*func)(int, ull *), int n, ull *ops, bool print)
{
    clock_t begin, end;
    
    // Record start time
    begin = clock();
    
    // Execute the function
    ull *series = func(n, ops);
    
    // Record end time
    end = clock();
    
    // Optionally print the series
    if (print)
    {
        printSeries(series, n);
    }
    
    // Free allocated memory
    free(series);
    
    // Calculate elapsed time in seconds
    // CLOCKS_PER_SEC is the number of clock ticks per second
    return (double)(end - begin) / CLOCKS_PER_SEC;
}

/**
 * Prints usage information for the program
 */
void help()
{
    printf("./fibonacci.out N [Type] [Print]\n");
    printf("\tN is the nth fibonacci number to generate, required.\n");
    printf("\t[Type] algorithm selection (default: 3):\n");
    printf("\t\t0 = iterative only\n");
    printf("\t\t1 = recursive only\n");
    printf("\t\t2 = dynamic programming only\n");
    printf("\t\t3 = all three algorithms (default)\n");
    printf("\t\t4 = iterative and DP only\n");
    printf("\t[Print] leave blank for timing only, or any value to print series\n");
}

/**
 * Main program entry point
 * Code adapted from: Dynamic Programming Lab/ Class Code
 * 
 */
int main(int argc, char *argv[])
{
    // Validate command line arguments
    if (argc < 2)
    {
        printf("Error: At least one argument needed (N)!\n");
        help();
        return 1;
    }

    // Parse command line arguments
    const int n = atoi(argv[1]);    // The nth fibonacci number
    
    // Validate n is positive
    if (n <= 0)
    {
        printf("Error: N must be a positive integer, got: %d\n", n);
        return 1;
    }
    
    // Validate n doesn't exceed our array limits
    if (n >= MAX)
    {
        printf("Error: N too large (max: %d), got: %d\n", MAX - 1, n);
        return 1;
    }
    
    int type = 3;                    
    bool print = false;              
    
    if (argc > 2)
    {
        type = atoi(argv[2]);
        // Validate type is in valid range
        if (type < 0 || type > 4)
        {
            printf("Error: Type must be 0-4, got: %d\n", type);
            return 1;
        }
    }
    if (argc > 3)
    {
        print = true;
    }

    // Initialize memoization table for DP algorithm
    for (int i = 0; i < MAX; i++)
    {
        table[i] = 0;
        initialized[i] = false;
    }

    ull ops;      // Operation counter
    double time;  // Execution time
    
    // Execute algorithm
    switch (type)
    {
    case 0:
        // Run iterative algorithm only
        printf("Iterative version\n");
        ops = 0;
        time = time_function(fibonacci_iterative, n, &ops, print);
        printf("Time: %f(%llu)\n", time, ops);
        break;
        
    case 1:
        // Run recursive algorithm only
        printf("Recursive version\n");
        ops = 0;
        time = time_function(fibonacci_r_full, n, &ops, print);
        printf("Time: %f(%llu)\n", time, ops);
        break;
        
    case 2:
        // Run dynamic programming algorithm only
        printf("Dynamic programming version\n");
        ops = 0;
        time = time_function(fibonacci_dp_full, n, &ops, print);
        printf("Time: %f(%llu)\n", time, ops);
        break;
        
    case 4:
        // Run iterative and DP for comparison (skip slow recursive)
        ops = 0;
        time = time_function(fibonacci_iterative, n, &ops, print);
        printf("%f,%llu,", time, ops);

        // Reset memoization table before running DP
        for (int i = 0; i < MAX; i++)
        {
            table[i] = 0;
            initialized[i] = false;
        }
        
        ops = 0;
        time = time_function(fibonacci_dp_full, n, &ops, print);
        printf("%f,%llu,-,-\n", time, ops);
        break;
        
    default:
        // Run all three algorithms (type == 3)
        // CSV format: time1,ops1,time2,ops2,time3,ops3
        
        // 1. Iterative
        ops = 0;
        time = time_function(fibonacci_iterative, n, &ops, print);
        printf("%f,%llu,", time, ops);

        // Reset memoization table before running DP
        for (int i = 0; i < MAX; i++)
        {
            table[i] = 0;
            initialized[i] = false;
        }
        
        // 2. Dynamic Programming
        ops = 0;
        time = time_function(fibonacci_dp_full, n, &ops, print);
        printf("%f,%llu,", time, ops);

        // 3. Recursive
        ops = 0;
        time = time_function(fibonacci_r_full, n, &ops, print);
        printf("%f,%llu\n", time, ops);
        break;
    }
    
    return 0;
}

