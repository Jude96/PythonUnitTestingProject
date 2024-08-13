
def setup_function(function):
    if function == test1:
        print('Setting up test1')
    elif function == test2:
        print('Setting up test2')
    else:
        print('Setting up unknown test')


def teardown_function(function):
    if function == test1:
        print('Tearing down test1')
    elif function == test2:
        print('Tearing down test2')
    else:
        print('Tearing down unknown test')


def test1():
    print('Executing test 1')
    assert True


def test2():
    print('Executing test 2')
    assert False