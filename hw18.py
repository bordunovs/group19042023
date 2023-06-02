def bold_string_return_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if isinstance(result, str):
            return f"<b>{result}</b>"
        return result
    return wrapper

@bold_string_return_decorator
def process_data(data):
    return data.upper()

print(process_data)

@bold_string_return_decorator
def calculate_sum(a, b):
    return a + b

print(process_data('fdhgfhgfgf/hyrt.vg'))
print(calculate_sum(123, 123))
