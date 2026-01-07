import time
import tracemalloc
def count_ways_to_summit(n):
    if n<=1:
        return 1
    prev2,prev1=1,1
    for _ in range(2,n+1):
        prev2,prev1 = prev1,prev1+prev2
    return prev1
n=int(input("Enter the total number of steps to reach the top ➡ : "))
if 1<=n<=45:
    start = time.perf_counter()
    tracemalloc.start()
    result = count_ways_to_summit(n)
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    end = time.perf_counter()
    print('The total number of unique ways to reach the summit ⛰ :', result)
    print("\nExecution time:", end - start, "seconds")
    print(f"Current memory usage: {current / 1024:.2f} KB")
    print(f"Peak memory usage: {peak / 1024:.2f} KB")
else:
    print("Enter steps in range of 1-45!")

