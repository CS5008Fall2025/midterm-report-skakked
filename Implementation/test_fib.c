#include <stdio.h>
#include <stdint.h>
#include <stdbool.h>
#include <stdlib.h>

#define MAX 50010
typedef uint64_t ull;

// Memoization table
static ull table[MAX];
static bool initialized[MAX] = {false};

// Copy your implementations here
ull fibonacci_dp(int n, ull *ops) {
    if (n <= 1) return n;
    if (initialized[n]) return table[n];
    (*ops)++;
    table[n] = fibonacci_dp(n - 1, ops) + fibonacci_dp(n - 2, ops);
    initialized[n] = true;
    return table[n];
}

ull fibonacci_r(int n, ull *ops) {
    if (n <= 1) return n;
    (*ops)++;
    return fibonacci_r(n - 1, ops) + fibonacci_r(n - 2, ops);
}

ull *fibonacci_iterative(int n, ull *ops) {
    ull *series = malloc(sizeof(ull) * n);
    if (n >= 1) series[0] = 1;
    if (n >= 2) series[1] = 1;
    for (int i = 2; i < n; i++) {
        (*ops)++;
        series[i] = series[i - 1] + series[i - 2];
    }
    return series;
}

void reset_table() {
    for (int i = 0; i < MAX; i++) {
        table[i] = 0;
        initialized[i] = false;
    }
}

int main() {
    int tests[] = {0, 1, 5, 10, 20, 30, 40};
    int num_tests = sizeof(tests) / sizeof(tests[0]);
    
    printf("Testing Fibonacci Implementations\n");
    printf("==================================\n\n");
    
    for (int i = 0; i < num_tests; i++) {
        int n = tests[i];
        ull ops = 0;
        
        printf("n = %d\n", n);
        
        // Iterative
        ops = 0;
        ull *iter_series = fibonacci_iterative(n == 0 ? 1 : n, &ops);
        ull iter_result = (n == 0) ? 0 : iter_series[n - 1];
        printf("  Iterative: %llu (ops: %llu)\n", iter_result, ops);
        free(iter_series);
        
        // Dynamic Programming
        reset_table();
        ops = 0;
        ull dp_result = fibonacci_dp(n, &ops);
        printf("  Dynamic:   %llu (ops: %llu)\n", dp_result, ops);
        
        // Recursive (skip for n > 30)
        if (n <= 30) {
            ops = 0;
            ull rec_result = fibonacci_r(n, &ops);
            printf("  Recursive: %llu (ops: %llu)\n", rec_result, ops);
            
            // Verify all match
            if (iter_result == dp_result && dp_result == rec_result) {
                printf("  ✓ All match\n");
            } else {
                printf("  ✗ MISMATCH!\n");
            }
        } else {
            printf("  Recursive: Skipped (n > 30)\n");
            if (iter_result == dp_result) {
                printf("  ✓ Iterative & DP match\n");
            }
        }
        
        printf("\n");
    }
    
    return 0;
}