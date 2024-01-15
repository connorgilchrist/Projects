master_pwd = input('Enter your master password')

def add():
    name = input('Account name: ')
    pwd = input('Password: ')
    #open file and automatically close it - append to it or create if file doesn't exist ('a')
    with open('passwords.txt', 'a') as f:
        f.write(name + ' | ' + pwd + '\n')

def view():
    with open('passwords.txt', 'r') as f:
        for line in f.readlines():
            print(line.rstrip())
    


while True:
    mode = input('Would you like to add a new password or view an existing one? (view, add), press q to quit').lower()
    if mode == 'q':
        break
    elif mode == 'view':
        view()
    elif mode == 'add':
        add()
    else:
        print('Not a valid input. Try again.')
        continue
     