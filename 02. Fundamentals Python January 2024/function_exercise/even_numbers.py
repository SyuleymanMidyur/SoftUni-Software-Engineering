def is_even(n):

    return n % 2 == 0


numbers = [int(num) for num in input().split()]
even_nums = list(filter(is_even, numbers))
print(even_nums)
