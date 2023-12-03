import time


def menu():
    print("1. Input Credentials")
    print("2. View Passwords")
    print("3. View Credit-Card")
    print("4. Exit")
    menu_selection = input("Please choose: ")

    if menu_selection == "1":
        print("Input Credentials")
        # Print user input, take entries, define as strings
        print("Please enter your credentials")
        input_url = input("url: ")
        print(input_url)

        input_user = input("user: ")
        print("Confirming:", input_url, " | ", input_user)

        # Requires Passwords to Match
        input_password = input("password: ")
        input_password_confirm = input("confirm password: ")
        if input_password != input_password_confirm:
            exit("Passwords do not match!")
        else:
            print("password match")
            print("\n")
            print("Commence to Credit-Card")
            # https://stackoverflow.com/questions/48817461/user-input-boolean-in-python

        user_cc_info_answer = input('Do you need to save a Credit-Card? (Y/N) : ').lower().strip() in ["yes", "y"]

        if user_cc_info_answer == "y":
            print("Credit-Card Numbers MUST be 16 characters")
            input_cc = input("Credit Card Number: ")
            if len(input_cc) == 16:
                print("Credit-Card ending in", input_cc[-4:], "Saved Successfully")
                user_cc_display = input_cc
                text_file = open("passwords.txt", "a")
                with open('passwords.txt', 'a') as file:
                    l0 = '\n'
                    l1 = input_url
                    l2 = input_user
                    l3 = input_password
                    l4 = input_cc
                text_file.writelines([l0, l1, " | ", l2, " | ", l3, " | ", l4])
                text_file.close()
                print("The following Information has been saved: (L49")
                # Important [-4:] colon must be AFTER -4 Digits or prior digits display Ref:
                # http://codepad.org/S3zjnKoD
                print("\n\n\n", input_url, "|", input_user, "|", "XXXX XXXX XXXX", user_cc_display[-4:])
                exit("Information Saved to file ")
            else:
                time.sleep(0.2)  # Wait for 3 Seconds #https://ioflood.com/blog/python-wait/
                print("*** Error! 16 characters are required! ***")
                time.sleep(1)  # Wait for 1 Seconds
                print("-> Please Try Again")
                time.sleep(1)  # Wait for 1 Seconds
                print("...")
                print(" ..")
                print("  .")
                menu()
        else:
            # Open File & Save user Input
            text_file = open("passwords.txt", "a")
            with open('passwords.txt', 'a') as file:
                l0 = '\n'
                l1 = "domain.com"  # input_url
                l2 = "user"  # input_user
                l3 = "pass"  # input_password
            text_file.writelines([l0, l1, " | ", l2, " | ", l3])
            text_file.close()
            print("The following Information has been saved:")
            print(input_url, "|", "User: ", input_user)
            exit("Information Saved to file ")

    elif menu_selection == "2":
        print("menu_level_2")
    else:
        print("menu_level_3")


menu()
