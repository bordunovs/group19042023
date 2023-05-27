def joke_selector(number):
    if number == 1:
        return "Чому зошит з математики виглядав сумно? Тому що було надто багато проблем!"
    elif number == 2:
        return "Хлопчик, який все дитинство провів із батьком на рибалці, так і не навчився розмовляти!"
    else:
        return "Чому кіт сидів за комп'ютером? Воно хотіло стежити за мишкою!"
print(joke_selector(3))

def calculate_perimeter(length, width):
    return 2.0 * (length + width)
print(calculate_perimeter(2, 5))

def clean_string(string):
    cleaned_string = string.replace('ї', '').replace('Ї', '').replace('ж', '').replace('Ж', '')
    return cleaned_string
print(clean_string('хижак та їжак'))

def remove_chars_from_target(target_string, remove_string):
    for char in remove_string:
        target_string = target_string.replace(char.lower(), '').replace(char.upper(), '')
    return target_string
target_string = 'хижак'
remove_string = 'вікно'
cleaned_string = remove_chars_from_target(target_string, remove_string)
print(cleaned_string)

def remove_chars_from_target(target_string, remove_string):
    cleaned_string = ""
    for char in target_string:
        if char not in remove_string:
            cleaned_string += char
    return cleaned_string
target_string = 'вОно'
remove_string = 'вікно'
cleaned_string = remove_chars_from_target(target_string, remove_string)
print(cleaned_string)







