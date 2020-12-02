# bucket_sort: https://www.cnblogs.com/kkun/archive/2011/11/23/bucket_sort.html

def bucket_sort(my_list: list) -> list:
    if len(my_list) == 0:
        return []
    
    min_value, max_value = min(my_list), max(my_list)
    bucket_count = int(max_value - min_value) + 1
    buckets = [[] for _ in range(bucket_count)]

    for i in range(len(my_list)):
        buckets[(int(my_list[i] - min_value) // bucket_count)].append(my_list[i])

    return [v for bucket in buckets for v in sorted(bucket)]

if __name__ == "__main__":
    assert bucket_sort([4, 5, 3, 2, 1]) == [1, 2, 3, 4, 5]
    assert bucket_sort([0, 1, -10, 15, 2, -2]) == [-10, -2, 0, 1, 2, 15]
