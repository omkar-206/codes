# ◈ 260907:0531

import time
import random
import string
import sys

# Increase recursion depth for QuickSort on large arrays
sys.setrecursionlimit(20000)

def Partition(m, p):
    v = a[m]
    i = m
    j = p
    
    while True:
        while True:
            i += 1
            if a[i] >= v: break
                
        while True:
            j -= 1
            if a[j] <= v: break
                
        if i < j:
            a[i], a[j] = a[j], a[i]
        else:
            break
            
    a[m] = a[j]
    a[j] = v
    return j

def QuickSort(p, q):
    if p < q:
        j = Partition(p, q + 1)
        QuickSort(p, j - 1)
        QuickSort(j + 1, q)

def get_sentinel(t):
    if t in ["Integers", "Floating Point"]:
        return float('inf')
    else:
        return chr(1114111)

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
        
        # Append sentinel value required by textbook QuickSort logic
        a.append(get_sentinel(t))
        
        start = time.perf_counter()
        QuickSort(0, n - 1)
        end = time.perf_counter()
        
        row_output += f" | {end - start:<10.6f}"
        
    print(row_output)