
class TestClass:
    @classmethod
    def setup_class(cls):
        print('Set up test class run before anything else in the class')

    @classmethod
    def teardown_class(cls):
        print('Teardown test class run at the tail end')

    def setup_method(self, method):
        if method == self.test1:
            print('\nSetting up test 1 \n')
        elif method == self.test2:
            print('\nSetting up test 2 \n')
        else:
            print('\nSetting up unknown test\n')

    def teardown_method(self, method):
        if method == self.test1:
            print('\nTearing down test 1 \n')
        elif method == self.test2:
            print('\nTearing downtest 2 \n')
        else:
            print('\nTearing down unknown test\n')


    def test1(self):
        print('Executing test 1')
        assert True

    def test2(self):
        print('Executing test 2')
        assert True