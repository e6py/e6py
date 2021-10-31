import sentinel

MISSING = sentinel.create(
    "MISSING",
    cls_dict={
        "__eq__": lambda x, y: x.__name__ == y.__name__ if hasattr(y, "__name__") else False,
        "__name__": "MISSING",
        "__getattr__": lambda x, y: None,
        "__bool__": lambda _: False,
    },
)
