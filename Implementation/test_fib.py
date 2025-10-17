
from fibonacci import fibonacci_iterative, fibonacci_dp, fibonacci_r

def test_fibonacci():
    """Test all three Fibonacci implementations"""
    test_values = [0, 1, 5, 10, 20, 30, 40]
    
    print("Testing Fibonacci Implementations")
    print("==================================\n")
    
    for n in test_values:
        print(f"n = {n}")
        
        # Iterative
        iter_result = fibonacci_iterative(n)
        print(f"  Iterative: {iter_result}")
        
        # Dynamic Programming (clear cache for accurate test)
        fibonacci_dp.cache_clear()
        dp_result = fibonacci_dp(n)
        print(f"  Dynamic:   {dp_result}")
        
        # Recursive (skip for n > 30 to avoid timeout)
        if n <= 30:
            rec_result = fibonacci_r(n)
            print(f"  Recursive: {rec_result}")
            
            # Verify all match
            if iter_result == dp_result == rec_result:
                print("  ✓ All match\n")
            else:
                print("  ✗ MISMATCH!\n")
        else:
            print("  Recursive: Skipped (n > 30)")
            if iter_result == dp_result:
                print("  ✓ Iterative & DP match\n")
            else:
                print("  ✗ MISMATCH!\n")

if __name__ == "__main__":
    test_fibonacci()