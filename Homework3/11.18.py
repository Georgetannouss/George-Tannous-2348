# George Tannous 1971969
# 11.18
lst = input().split()

nums = [int(num) for num in lst]

non_neg_nums = [num for num in nums if num >= 0]

sorted_nums = sorted(non_neg_nums)

output = ' '.join(str(num) for num in sorted_nums) + ' '

print(output, end='')
