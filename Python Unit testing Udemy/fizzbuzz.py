
def fizzBuzz(num: int) -> str:
    match num:
        case _ if num % 3 == 0 and num % 5 == 0:
            return 'FizzBuzz'
        case _ if num % 3 == 0:
            return 'Fizz'
        case _ if num % 5 == 0:
            return 'Buzz'
        case _:
            return f'{num} is not a multiple of 3, 5 or of both 3 and 5'


num = int(input('Enter an integer number:- '))
print(fizzBuzz(num))


