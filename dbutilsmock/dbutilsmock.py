from typing import Dict
from unittest.mock import MagicMock


class DbutilsMock():
    """Simple Mock for dbutils functions that can be used whenever dbutils is not available, e.g. for unittesting databricks notebooks locally
    
    Use in the following way:
    Before your test initiate the dbutils Mock:
    ```
    from dbutilsmock.dbutilsmock import DbutilsMock
    dbutils = DbutilsMock(
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
    ```
    Then in your test code the following code should work:
    ```
    >>>dbutils.widgets.text(name="widget_name", defaultValue="defaultWidgetValue", label="WidgetLabel")
    >>>dbutils.widgets.get("input_path")
    '/test/asd'
    >>>dbutils.secrets.get("my_scope", "my_key")
    'the_real_secret'
    ```

    In case you want to test the function `random_number` in a notebook like this:
    ```
    from random import random

    path = dbutils.widgets.get("input_path")

    def random_number():
        r = random()
        print(r)
        return r
    ```

    You can inject dbutils in the test for that notebook by using the following code:

    ```
    from dbutilsmock.dbutilsmock import DbutilsMock
    import unittest

    class TestNotebookMethods(unittest.TestCase):
        def setUp(self):
            import builtins
            builtins.dbutils = DbutilsMock(
                widgets_dict={
                    "input_path": "/in/test"
                }
            )

        def test_random_number(self):
            from tests.notebook_with_dbutils import random_number
            self.assertIsInstance(random_number(), float)
    ```

    The previous error `NameError: name 'dbutils' is not defined` will be solved and you can test your function.
    """
    widgets = MagicMock()
    secrets = MagicMock()

    def __init__(self, widgets_dict: Dict = None, secrets_dict: Dict = None):
        self.widgets.text = MagicMock(return_value=None)

        if widgets_dict:
            self.widgets._widgets_dict = widgets_dict
            self.widgets.get = self._dbutils_widgets_get

        if secrets_dict:
            self.secrets._secrets_dict = secrets_dict
            self.secrets.get = self._dbutils_secrets_get

    def _dbutils_widgets_get(self, text):
        if self.widgets._widgets_dict:
            return self.widgets._widgets_dict[text]
        else:
            return text

    def _dbutils_secrets_get(self, scope, key):
        if self.secrets._secrets_dict:
            return self.secrets._secrets_dict[scope][key]
        else:
            return f"{scope}_{key}"


if __name__ == "__main__":
    dbutils = DbutilsMock(
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

    dbutils.widgets.text(name="widget_name", defaultValue="defaultWidgetValue", label="WidgetLabel")
    dbutils.widgets.get("input_path")

    dbutils.secrets.get("my_scope", "my_key")

    dbutils = DbutilsMock()
