import multiprocessing
import math
import time
import sys

sys.set_int_max_str_digits(100000)

# Function to compute factorial of a given number
def compute_factorial(number):
    print(f'Computing factorial of number {number}')
    result = math.factorial(number)
    print(f'Factorial of {number} is computed')
    return result

if __name__ == '__main__':
    numbers = [5000, 600, 7000]  # List of numbers for which to compute the factorials
    start_time = time.time()  # Record the start time

    # Create a pool of worker processes
    with multiprocessing.Pool() as pool:
        results = pool.map(compute_factorial, numbers)  # Map numbers to compute_factorial function

    end_time = time.time()  # Record the end time
    
    # Output the results
    print(f'Start time: {start_time}')
    print(f'End time: {end_time}')
    print(f'Results: {results}')
    print(f'Time taken: {end_time - start_time} seconds')