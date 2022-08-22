#Nicholas Clarke
#Aug 3, 2022
#lab 7
#Password checker


import checker

def main():
    # Sudo apt get!
    password = input("Enter your password: ")

    while not checker.valid_password(password):
        print("Sorry try again!!!")
        password = input("Enter your password: ")

    print("Entered Passphrase is VALID!")

    main()
