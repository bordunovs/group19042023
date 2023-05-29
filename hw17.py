def generate_number_list(start):
    if start < 1:
        raise ValueError("Початкове значення повинно бути позитивним числом")
    return [num for num in range(start, start+10)]

start = 1
number_list = generate_number_list(start)
print(number_list)
start = 5
number_list = generate_number_list(start)
print(number_list)
