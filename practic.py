admin = {
    'name': 'Alex',
    'password': '1234',
}

def protection(func):
    def wrapper(*args, **kwargs):
        user = input('enter your name >> ')
        password = input('enter password >> ')
        if user == admin['name'] and password ==['password']:
            result = func(*args, **kwargs)
            return result
        else:
            return {'message': 'access prohibited'}
    return wrapper

# def notify_dec(func):
#     def wrapper(*args, **kwargs):


@protection
def mult_two(value):
    return  value * 2

@protection
def convert_to_string(value):
    return  str(value)




def mult_two(value):
    return value * 2


def convert_to_string(value):
    return str(value)


print(mult_two(55))
print(mult_two(66))
print(mult_two(77))

print(convert_to_string(6555665))
print(type(convert_to_string([5, 6])))


# def write_to_file(file_name: str):
#
#     with open()
#
#     pass
