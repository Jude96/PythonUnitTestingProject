import pytest

def fizzBuzz(num):
    match num:
        case _ if num % 3 == 0 and num % 5 == 0:
            return 'FizzBuzz'
        case _ if num % 3 == 0:
            return 'Fizz'
        case _ if num % 5 == 0:
            return 'Buzz'
        case _:
            return str(num)   #f'{num} is not a multiple of 3, 5 or of both 3 and 5'
    #return "1"


#tests written before code is written

def test_CanCall_FizzBuzz():
    fizzBuzz(1)

def testReturns1When1Passed():
    retVal = fizzBuzz(1)
    assert retVal == "1"#has to return true otherwise an assertion error pops up


def testFizzReturnedWhenMutipleof3Passed():
    retVal = fizzBuzz(3)
    assert retVal == "Fizz"





def choose_test_option():
    choice = input('Enter test choice option\n 1. Test Can Call Func \n2. Test Returns 1 when 1 Passed:-  ')
    match choice:
        case "1":
            test_CanCall_FizzBuzz()
        case "2":
            testReturns1When1Passed()
        case _:
            print('Wrong input, Enter the number')

choose_test_option()