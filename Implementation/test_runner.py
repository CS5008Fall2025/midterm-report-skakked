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

