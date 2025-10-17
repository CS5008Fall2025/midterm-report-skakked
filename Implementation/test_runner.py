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
        values (list): List of result rows, each containing
                      [iterative, dp, recursive] data
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



