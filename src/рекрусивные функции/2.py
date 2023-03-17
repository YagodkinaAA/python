def recursive_digit_sum(num):
    if num == 0:
        return 0
    else:
        # (a // b, a % b)
        (d, r) = divmod(num, 10)
        return recursive_digit_sum(d) + r


print(recursive_digit_sum(123))
