def fizzBuzz(n: int):
    return [
        'Fizz' if x % 3 == 0
        else 'Buzz' if x % 5 == 0
        else 'FizzBuzz' if x % 15 == 0
        else x
        for x in range(1, n + 1)
    ]
