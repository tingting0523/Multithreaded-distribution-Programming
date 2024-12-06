import time
import threading
import json
import numpy as np  

def FloatOperations(n):
    sum = 0.0
    for i in range(n):
        sum += (i * 0.6) / 0.5
    return sum

def IntOperations(n):
    sum = 0
    for i in range(n):
        sum += (i * 2)
    return sum

# calculate Giga FLOPS
def CalculationFlops(num_operations):
    start_time = time.perf_counter()  # execute start time

    # float operations
    sum = FloatOperations(num_operations)

    end_time = time.perf_counter()  # execute end time

    # calculate elapsed time
    elapsed_time = end_time - start_time  # unit:s

    # calculate Giga FLOPS
    giga_flops = num_operations / elapsed_time / 1e9  # change the num of operations to Giga
    return giga_flops, start_time, end_time

# calculate Giga IOPS
def CalculationIops(num_operations):
    start_time = time.perf_counter()  # execute start time

    # int operations
    sum = IntOperations(num_operations)

    end_time = time.perf_counter()  # execute end time

    # calculate elapsed time
    elapsed_time = end_time - start_time  # unit:s

    # calculate Giga IOPS
    giga_iops = num_operations / elapsed_time / 1e9  # change the num of operations to Giga
    return giga_iops, start_time, end_time

# create thread
class BenchmarkThread(threading.Thread):
    def __init__(self, num_operations):
        threading.Thread.__init__(self)
        self.num_operations = num_operations
        self.flops = None
        self.iops = None
        self.flops_start_time = None
        self.flops_end_time = None
        self.iops_start_time = None
        self.iops_end_time = None

    def run(self):
        self.flops, self.flops_start_time, self.flops_end_time = CalculationFlops(self.num_operations)
        self.iops, self.iops_start_time, self.iops_end_time = CalculationIops(self.num_operations)

lock = threading.Lock()
shared_resource = 0

num_operations = 5000000  # the num of operations
num_threads_list = [1, 2, 4, 8]  # num of threads
benchmark_data = []  # benchmark result
num_runs = 3   

# outer loop : Iterate thread counts
for num_threads in num_threads_list:
    flops_results = []
    iops_results = []

    # middle loop: Run the benchmark num_runs times to calculate the mean and standard deviation
    for _ in range(num_runs):
        threads = []
        total_flops = 0
        total_iops = 0

        # inner loop create and run thread
        for _ in range(num_threads):
            thread = BenchmarkThread(num_operations)
            threads.append(thread)
            thread.start()
            with lock:  # Use locks to secure access to shared resources
                shared_resource += 1  # Update the Commons

        # Wait for all threads to complete and collect the results
        for thread in threads:
            thread.join()
            total_flops += thread.flops
            total_iops += thread.iops

            # Print the FLOPS and IOPS start and end times for each thread
            print(f"Thread finished FLOPS at {thread.flops_end_time:.6f}, started at {thread.flops_start_time:.6f}")
            print(f"Thread finished IOPS at {thread.iops_end_time:.6f}, started at {thread.iops_start_time:.6f}")

        # Calculate the average of the performance of a single benchmark
        avg_flops = total_flops / num_threads
        avg_iops = total_iops / num_threads

        flops_results.append(avg_flops)
        iops_results.append(avg_iops)

    # Calculate the mean and standard deviation of FLOPS and IOPS: The average of performance across multiple benchmarks, reflecting more stable performance metrics
    flops_mean = np.mean(flops_results)
    flops_std = np.std(flops_results)
    iops_mean = np.mean(iops_results)
    iops_std = np.std(iops_results)

    print(f"With {num_threads} thread(s):")
    print(f"  Average Giga FLOPS: {avg_flops}")
    print(f"  Average Giga IOPS: {avg_iops}")
    print(f"  FLOPS: Mean = {flops_mean}, Std Dev = {flops_std}")
    print(f"  IOPS: Mean = {iops_mean}, Std Dev = {iops_std}")

    benchmark_data.append({
        "num_threads": num_threads,
        "avg_flops": avg_flops,
        "avg_iops": avg_iops,
        "flops_mean": flops_mean,
        "flops_std": flops_std,
        "iops_mean": iops_mean,
        "iops_std": iops_std
    })

with open("/Users/jolie/Desktop/school/98-SCSU/3-course-563/project assignment 1/benchmark_data.json", 'w') as json_file:
    json.dump(benchmark_data, json_file, indent=4)

print("Benchmark data has been saved to benchmark_data.json.")
