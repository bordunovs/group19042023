login = input('enter your login (only letters) >>> ')

password = input('enter password(only letters and numbers) >>> ')

repeat_password = input('repeat password entry >>>')

true = True
false = False

print(bool(password == repeat_password))
#if login:
    #print(login)
if password == repeat_password:
    print('user is logged in')
elif password != repeat_password:
    print('incorrect')

print('')
