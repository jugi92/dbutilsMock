# dbutilsMock
Simple Mock for dbutils functions that can be used whenever dbutils is not available, e.g. for unittesting databricks notebooks locally
    
Use in the following way:
Before your test initiate the dbutils Mock:
```
from DbutilsMock import DbutilsMock
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