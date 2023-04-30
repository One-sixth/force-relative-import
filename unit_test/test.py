import unittest

from force_relative_import import enable_force_relative_import, global_enable_force_relative_import, global_disable_force_relative_import


class TestActs(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def test_1(self):
        print('Test 1')
        self.assertTrue(True)
        with enable_force_relative_import():
            from ._test_module import return_good
            self.assertTrue(return_good() == 'good')
        print()

    def test_2(self):
        print('Test 2')
        global_enable_force_relative_import()

        from ._test_module import return_good
        self.assertTrue(return_good() == 'good')

        global_disable_force_relative_import()
        try:
            from ._test_module import return_good
            self.assertTrue(False)
        except ImportError:
            self.assertTrue(True)
        print()

    def test_3(self):
        print('Test 3')
        from force_relative_import import enable_now
        from ._test_module import return_good

        self.assertTrue(return_good() == 'good')
        self.assertTrue(True)
        print()


if __name__ == '__main__':
    unittest.main()
