#George Tannous 1971969
#14.13

num_calls = 0


def partition(user_ids, i, k):
    pivot_idx = (i + k) // 2
    pivot = user_ids[pivot_idx]
    l = i
    h = k
    while l <= h:
        while user_ids[l] < pivot:
            l += 1
        while user_ids[h] > pivot:
            h -= 1
        if l <= h:
            user_ids[l], user_ids[h] = user_ids[h], user_ids[l]
            l += 1
            h -= 1
    return l


def quicksort(user_ids, i, k):
    global num_calls
    num_calls += 1
    if i >= k:
        return
    else:
        pivot_idx = partition(user_ids, i, k)
        quicksort(user_ids, i, pivot_idx - 1)
        quicksort(user_ids, pivot_idx, k)


if __name__ == "__main__":
    user_ids = []
    user_id = input()
    while user_id != "-1":
        user_ids.append(user_id)
        user_id = input()

    # Initial call to quicksort
    quicksort(user_ids, 0, len(user_ids) - 1)

    # Print number of calls to quicksort
    print(num_calls)

    # Print sorted user ids
    for user_id in user_ids:
        print(user_id)
