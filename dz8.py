login = input('enter your login (only letters) >>> ')
password = input('enter password(only letters and numbers) >>> ')
contains_login_only_letters = login.isalpha()
contains_password_only_numbers_letters = password.isalnum()

if contains_login_only_letters and contains_password_only_numbers_letters:
    confirm_password = input('confirm_password:')
    if password == confirm_password:
        print('You are succesfully login')
        print('The user is disconnected due to the whims of the teacher')
        
        username_again_login = input('enter your login (only letters) >>> ')
        password_again_login = input('enter password(only letters and numbers) >>> ')
        if password_again_login == password and username_again_login == login:
            print('You are succesfully login')
        else:
            print('login or password incorrect')







