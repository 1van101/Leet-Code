def reverse(x):
    new_num = ''
    is_negative = False
    for num in (str(abs(x))[::-1]):
        if num == '-':
            is_negative = True
        new_num += num

    x = int(new_num.lstrip('0'))

    if is_negative:
        x -= 2 * x
    if int(x) > 2**32 - 1:
        return 0
    else:
        return x


print(reverse(0))
