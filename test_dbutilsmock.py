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

def test_widgets_text():
    assert dbutils.widgets.text(name="widget_name", defaultValue="defaultWidgetValue", label="WidgetLabel") is None

def test_widgets_get():
    assert dbutils.widgets.get("input_path") == '/test/asd'

def test_secrets_get():
    assert dbutils.secrets.get("my_scope", "my_key") == 'the_real_secret'