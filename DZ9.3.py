int_text = input('введите любой текст,с маленьких и заглавных букв >>> ')
int_text_result = []
for element in int_text:
 if element.isupper():

    int_text_result.append(element)
print(int_text_result)