"""
Test Runner for Fibonacci Series Implementations

Name: Siddharth Kakked
Date: 14th October 2025
Runs tests on different Fibonacci implementations and logs performance metrics.
"""
import subprocess
import sys
import csv
import argparse
import os

# Detect platform and set appropriate executable name
if os.name == 'nt':  # Windows
    EXEC = "fibonacci.exe"
else:  # Other
    EXEC = "./fibonacci"
    
TIMEOUT = 60                          # Timeout in seconds (prevents infinite loops)
OUT_DEFAULT = "fibonacci_run.csv"     # Default output filename
OUT_FILE_TIME = "timings_"            # Prefix for timing results file
OUT_FILE_OPS = "ops_"                 # Prefix for operations results file
CSV_HEADER = "N,Iterative,Dynamic Programming,Recursive"  # Column headers

class RecursionTimeoutError(Exception):
    """
    Timeout error for recursive fibonacci implementation
    """
    pass

def run_single(n: int, typ: int) -> dict:
    """
    Executes a single test run of the fibonacci program.
    
    Args:
        n (int): The nth fibonacci number to generate
        typ (int): Algorithm type to use:
                   0 = iterative
                   1 = recursive  
                   2 = dynamic programming
                   3 = all three algorithms
                   4 = iterative and DP only

    Returns:
        dict: Dictionary with two keys:
              - 'timings': list of execution times [iterative, dp, recursive]
              - 'operations': list of operation counts [iterative, dp, recursive]

    Raises:
        RecursionTimeoutError: If execution exceeds TIMEOUT seconds
        Exception: If subprocess returns non-zero exit code
    """
    try:
        # Build command string and execute
        command = f"{EXEC} {n} {typ}"
        results = subprocess.run(
            command.split(),           # Split command into list for subprocess
            timeout=TIMEOUT,           # Kill process if it runs too long
            capture_output=True,       # Capture stdout and stderr
            text=True                  # Return output as strings, not bytes
        )
    except subprocess.TimeoutExpired:
        # Timeout usually means recursive algorithm is taking too long
        raise RecursionTimeoutError(f"Timeout of {TIMEOUT} seconds reached for n={n}")

    # Check if program executed successfully
    if results.returncode != 0:
        raise Exception(f"Error running n={n}: {results.stderr}")

    # Parse comma-separated output
    # Expected format: time1,ops1,time2,ops2,time3,ops3
    # Or for type 4: time1,ops1,time2,ops2,-,-
    results_line = results.stdout.strip().split(",")
    
    timings = []      # Store execution times
    operations = []   # Store operation counts
    
    # Parse pairs of (time, ops) from output
    for i in range(0, len(results_line), 2):
        timings.append(results_line[i])
        operations.append(results_line[i + 1])

    return {"timings": timings, "operations": operations}

def save_to_csv(values: list, out_file: str, step: int):
    """
    Saves collected data to a CSV file with proper headers.
    
    Args:
        values (list): List of result rows to write
        out_file (str): Output filename to write to
        step (int): Step size used in testing (for calculating N values)
    """
    with open(out_file, "w", newline="") as f:
        csv_writer = csv.writer(f)
        
        # Write header row
        csv_writer.writerow(CSV_HEADER.split(","))
        
        # Write data rows with N values
        for i, row in enumerate(values):
            # Calculate actual N value: starts at 1, increments by step
            n_value = i * step + 1
            row_with_n = [n_value] + row
            csv_writer.writerow(row_with_n)

def main(n: int, step: int = 1, out_file: str = OUT_DEFAULT):
    """
    Main execution function that runs the complete test suite.
    
    Args:
        n (int): Maximum fibonacci number to test
        step (int): Increment between test values 
        out_file (str): Base filename for output CSVs
    
    Output:
        Creates two CSV files:
        - ops_<out_file>: Operation counts for each algorithm
        - timings_<out_file>: Execution times for each algorithm
    """
    # Start by testing all three algorithms (type 3)
    run_type = 3
    
    # Storage for results
    results = {
        "timings": [],      # List of timing rows
        "operations": []    # List of operation count rows
    }
    
    # Run tests with increasing n values
    for i in range(1, n + 1, step):
        try:
            # Execute single test
            result = run_single(i, run_type)
            
            # Store results
            results["timings"].append(result["timings"])
            results["operations"].append(result["operations"])
            
        except RecursionTimeoutError as e:
            # Recursive algorithm timed out - switch to iterative+DP only
            print(f"Timeout at n={i}, switching to iterative and DP only", file=sys.stderr)
            run_type = 4  # Type 4 = iterative and DP only, skip recursive
            
            # Retry current n with new run type
            result = run_single(i, run_type)
            results["timings"].append(result["timings"])
            results["operations"].append(result["operations"])
            
        except Exception as e:
            # Other error occurred - print and stop testing
            print(e, file=sys.stderr)
            break
    
    # Save results to CSV files
    save_to_csv(results["operations"], OUT_FILE_OPS + out_file, step)
    save_to_csv(results["timings"], OUT_FILE_TIME + out_file, step)
    
    # Inform user where results were saved
    print(f"Results saved to {OUT_FILE_OPS + out_file} and {OUT_FILE_TIME + out_file}")

if __name__ == "__main__":
    # Configure command line argument parser
    parser = argparse.ArgumentParser(
        description="Run the fibonacci series program with multiple test cases"
    )
    
    # Required positional argument: maximum n to test
    parser.add_argument(
        "n", 
        type=int, 
        help="The maximum nth fibonacci number to test"
    )
    
    # Optional arguments
    parser.add_argument(
        "--step", 
        type=int, 
        default=1, 
        help="Step size between test values (default: 1)"
    )
    parser.add_argument(
        "--out", 
        type=str, 
        default=OUT_DEFAULT, 
        help=f"Base output filename (default: {OUT_DEFAULT})"
    )
    parser.add_argument(
        "--timeout", 
        type=int, 
        default=TIMEOUT, 
        help=f"Timeout in seconds for each test (default: {TIMEOUT})"
    )
    parser.add_argument(
        "--exec", 
        type=str, 
        default=EXEC, 
        help=f"Executable to run (default: {EXEC}). Use 'python3 fibonacci.py' for Python version"
    )
    
    # Parse command line arguments
    args = parser.parse_args()
    
    # Update global configuration with command line arguments
    TIMEOUT = args.timeout
    EXEC = args.exec
    
    # Run the test suite
    main(args.n, args.step, args.out)
    

