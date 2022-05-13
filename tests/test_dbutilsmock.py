import unittest
from dbutilsmock.dbutilsmock import DbutilsMock


class TestDbutilsMethods(unittest.TestCase):
    def setUp(self):
        import builtins
        builtins.dbutils = DbutilsMock(
            widgets_dict={
                "input_path": "/test/asd",
                "out_path": "/out/test"
            },
            secrets_dict={
                "my_scope": {
                    "my_key": "the_real_secret"
                }
            }
        )

    def test_widgets_text(self):
        assert dbutils.widgets.text(name="widget_name", defaultValue="defaultWidgetValue", label="WidgetLabel") is None

    def test_widgets_get(self):
        assert dbutils.widgets.get("input_path") == '/test/asd'

    def test_secrets_get(self):
        assert dbutils.secrets.get("my_scope", "my_key") == 'the_real_secret'


if __name__ == '__main__':
    unittest.main()
