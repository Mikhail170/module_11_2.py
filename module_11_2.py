class Introspection:
    def __init__(self, obj):
        self.obj = obj

    def get_info(self):
        obj_type = type(self.obj)
        attributes = dir(self.obj)
        methods = [attr for attr in attributes]
        module = getattr(self.obj, '__module__', 'builtins')  # 'builtins' для встроенных типов

        info = {
            "type": obj_type,
            "attributes": attributes,
            "methods": methods,
            "module": module,
        }

        return info

    def __str__(self):
        return str(self.get_info())


number_info = Introspection(42)
print(number_info)

string_info = Introspection("Hello")
print(string_info)

list_info = Introspection([1, 2, 3])
print(list_info)

dict_info = Introspection({"key": "value"})
print(dict_info)
