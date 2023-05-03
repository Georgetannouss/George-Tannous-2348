# George Tannous 1971969
# 14.11

def selection_sort_descend_trace(lst):
    for i in range(len(lst)):
        max_idx = i
        for j in range(i + 1, len(lst)):
            if lst[j] > lst[max_idx]:
                max_idx = j
        lst[i], lst[max_idx] = lst[max_idx], lst[i]
        if i != len(lst) - 1:
            print(' '.join(str(x) for x in lst), '')


def main():
    lst = [int(x) for x in input().split()]
    selection_sort_descend_trace(lst)


if __name__ == '__main__':
    main()
