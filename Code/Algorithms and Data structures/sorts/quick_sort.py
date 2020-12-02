# 快排, 分而治之

def quick_sort(collection: list) -> list:
    if len(collection) < 2:
        return collection

    pivot = collection.pop()
    greater, lesser = [], []

    for i in collection:
        (greater if i > pivot else lesser).append(i)

    return quick_sort(lesser) + [pivot] + quick_sort(greater)


if __name__ == "__main__":
    print(quick_sort([1, 3, 2, 4, 5]))
