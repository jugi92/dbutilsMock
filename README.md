# dbutilsMock
Simple Mock for dbutils functions that can be used whenever dbutils is not available, e.g. for unittesting databricks notebooks locally

Use in the following way:
Before your test initiate the dbutils Mock:
```
from dbutilsmock import DbutilsMock
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
from dbutilsmock import DbutilsMock
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
        from notebook_with_dbutils import random_number
        self.assertIsInstance(random_number(), float)
```

The previous error `NameError: name 'dbutils' is not defined` will be solved and you can test your function.
   