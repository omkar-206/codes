# ◈ 260907:0400

import time
import random
import string

def MergeSort(low, high):
    if low < high:
        mid = (low + high) // 2
        MergeSort(low, mid)
        MergeSort(mid + 1, high)
        Merge(low, mid, high)

def Merge(low, mid, high):
    h = low
    i = low
    j = mid + 1
    
    while h <= mid and j <= high:
        if a[h] <= a[j]: 
            b[i] = a[h]
            h += 1
        else:
            b[i] = a[j]
            j += 1
        i += 1

    if h > mid:
        for k in range(j, high + 1):
            b[i] = a[k]
            i += 1
    else:
        for k in range(h, mid + 1):
            b[i] = a[k]
            i += 1
            
    for k in range(low, high + 1):
        a[k] = b[k]

sizes = [1000, 2500, 5000, 7500, 10000]
types = ["Integers", "Floating Point", "Alphabets", "Strings"]

# Print the table header
print(f"{'Type / Size':<16} | {'1000':<10} | {'2500':<10} | {'5000':<10} | {'7500':<10} | {'10000':<10}")
print("-" * 81)

# Loop through types (rows) first, then sizes (columns)
for t in types:
    row_output = f"{t:<16}"
    
    for n in sizes:
        if t == "Integers":
            a = [random.randint(1, 10000) for _ in range(n)]
        elif t == "Floating Point":
            a = [random.random() for _ in range(n)]
        elif t == "Alphabets":
            a = [random.choice(string.ascii_letters) for _ in range(n)]
        elif t == "Strings":
            a = ["".join(random.choices(string.ascii_letters, k=5)) for _ in range(n)]
        
        b = [None] * n
        
        start = time.perf_counter()
        MergeSort(0, n - 1)
        end = time.perf_counter()
        
        row_output += f" | {end - start:<10.6f}"
        
    print(row_output)