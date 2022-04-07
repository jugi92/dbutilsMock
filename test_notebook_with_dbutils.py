from dbutilsmock import DbutilsMock
import unittest

class TestNotebookMethods(unittest.TestCase):
    def setUp(self):
        import builtins
        builtins.dbutils = DbutilsMock(
            widgets_dict={
                "input_path": "/in/test",
                "out_path": "/out/test"
            },
            secrets_dict={
                "my_scope": {
                    "my_secret": "the_real_secret"
                }
            }
        )

    def test_random_number(self):
        from notebook_with_dbutils import random_number
        self.assertIsInstance(random_number(), float)

if __name__ == '__main__':
    unittest.main()
