#if divisble by 3, print fizz
#if divisible by 5, print buzz
#if divisible by 3 AND 5, fizzbuzz
#anything else, return input

def fizz_buzz(input):
    if (input % 3 == 0) and (input % 5 == 0):
        return "FizzBuzz"
    if input % 3 == 0:
        return "Fizz"
    if input % 5 == 0:
        return "Buzz"
    return input

print(fizz_buzz(7))