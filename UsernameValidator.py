
def Registration():
    registered = False
    while not registered:
        username = input('What is your name? ')
        if len(username) < 3:
            print('Your Username must be 3-15 characters long')
            print(' ')
        elif len(username) > 15:
            print('Your username must be 3-15 characters long')
            print(' ')
        else:
            hassymbol = False
            for i in username:
                for x in '?.></':
                    if i == x:
                        hassymbol = True
            if hassymbol:
                print('Contains invalid symbols')
                print(' ')
            else:
                print('Welcome %s, thanks for registering'%username)
                break
                

Registration()