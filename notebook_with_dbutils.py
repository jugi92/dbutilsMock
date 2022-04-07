from random import random

dbutils.widgets.get("input_path")

def random_number():
    r = random()
    print(r)
    return r
