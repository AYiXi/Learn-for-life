# QuickSort
```py
quicksort = lambda l: quicksort([i for i in l[1:] if i < l[0]]) + [l[0]] + quicksort([j for j in l[1:] if j >= l[0]]) if l else []
```