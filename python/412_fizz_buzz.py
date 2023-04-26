def fizzBuzz(n: int):

    return [
        'Fizz' if x % 3 == 0
        else 'Buzz' if x % 5 == 0
        else 'FizzBuzz' if x % 15 == 0
        else x
        for x in range(1, n + 1)
    ]


answer = []
for i in range(1, n + 1):
    if i % 15 == 0:
        answer.append('FizzBuzz')
    elif i % 3 == 0:
        answer.append('Fizz')
    elif i % 5 == 0:
        answer.append("Buzz")
    else:
        answer.append(str(i))
return answer

print(fizzBuzz(10))
