login = input('enter your login (only letters) >>> ')

password = input('enter password(only letters and numbers) >>> ')

repeat_password = input('repeat password entry >>>')

true = True
false = False


if login.isalpha() and password == repeat_password:
    print('user is extended at the whim of the instructor , repeat login and password')

else:

    print('incorrect')

log1 = input('enter your login (only letters) >>> ')

pas1 = input('enter password(only letters and numbers) >>> ')

pas2 = input('repeat password entry >>>')

true = True

false = False

if password == pas1:
    print('user is logged in')
if log1 == login:
    print('user is logged in')
if log1 != login:
    print('password and login not correct')
