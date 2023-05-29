some_list = [5, 6, 18, 0, -6, 7, 7, 7, 8]

number = 6655

target_list = []
for number in some_list:
    if number > 5:
        target_list.append(number)

print(target_list)
print(number)

# comprehension

new_target_list = [number_inner for number_inner in some_list if number_inner > 5]
print(new_target_list)
# print(number_inner) error

new_target_list = {number_inner for number_inner in some_list if number_inner > 5}
print(new_target_list)

list_dif_types = [[1], [2, 3], 'abc', 5]

list_comp_double = [element * 2 for element in list_dif_types]
print(list_comp_double)

list_comp_double_pairs = {str(element): element * 2 for element in list_dif_types}
print(list_comp_double_pairs)

list_comp_double_numbers = {element: element * 2 for element in some_list}
print(list_comp_double_numbers)


some_string = 'agsfdyafeydaygYFTFVjyYBYuiuigyy'

list_lower_case = [char for char in some_string if char.islower()]

print(list_lower_case)

list_lower_case_converted_to_upper = [char.upper() for char in some_string if char.islower()]
print(list_lower_case_converted_to_upper)



