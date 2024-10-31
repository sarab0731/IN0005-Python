import user
import admin

print("Are you a user or admin?")
while True:
    try:
        mode = int(input("To select user mode, enter 1.\nTo select admin mode, enter 2:\n"))
        if mode not in (1, 2):
            raise ValueError("Invalid input. Please enter 1 or 2.")
        break  # Exit the loop if input is valid
    except ValueError as e:
        print(e)

if mode == 1:
    while True:
        try:
            register_or_login = int(input("To login to your account, enter 1.\nTo create a new account, enter 2:\n"))
            if register_or_login not in (1, 2):
                raise ValueError("Invalid input. Please enter 1 or 2.\n")
            break  # Exit the loop if input is valid
        except ValueError as e:
            print(e)
        
    if register_or_login == 1:
        username = user.login()
    elif register_or_login == 2:
        username = user.register()
    
    user.menu(username)

elif mode == 2:
    admin.menu()
