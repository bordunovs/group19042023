first_name = input("Please enter your first name: ").title()
last_name = input("Please enter your last name: ").upper()

result = f"Hello, {first_name} {last_name}, did you know that your name consists of {len(first_name ) } letters"

result = result.replace("Hello", "Hi")

result += "?"

print(result)
