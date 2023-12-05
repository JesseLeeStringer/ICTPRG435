"""
User ID: S8102226
Student: Jesse-Lee Stringer
Unit: ICTPRG435
Development Date: 03/12/2023
Source: https://github.com/JesseLeeStringer/ICTPRG435
"""
import time  # Need it for "Sleep"
from colorama import Fore, Back, Style  # Let's create notifications with Colour, and Reset Styles
import art  # Art work for Option #3/4
from art import *  # Let's import all the art works


def menu():  # Give the user an option of four choices.
    print("1. Input Credentials")
    print("2. View Passwords")
    print("3. View Credit-Card")
    print("4. Exit")
    menu_selection = input("Please select 1-4: ")

    if menu_selection == "1":
        print("Input Credentials")
        # Print user input, take entries, define as strings
        print("Please enter your credentials")
        input_url = input("url: ")
        print(input_url)

        input_user = input("user: ")
        print("Confirming:", input_url, " | ", input_user)

        # Requires Passwords to Match
        input_password = input("Password: ")
        input_password_confirm = input("Confirm Password: ")
        if input_password != input_password_confirm:
            exit("Passwords do not match!")
        else:
            print(Fore.RED + "Password Confirmed" + "\n")  # Give User feedback on progress
            print(Style.RESET_ALL + "Commence to Credit-Card")  # Reset Styling & Progression

        # https://stackoverflow.com/questions/48817461/user-input-boolean-in-python
        user_cc_info_answer = input('Do you need to save a Credit-Card? (Y/N) : ').lower().strip()

        if user_cc_info_answer == 'y':
            print("\n" + "Credit-Card Numbers MUST be 16 characters")
            input_cc = input("Credit Card Number: ")

            # https://stackoverflow.com/questions/40688156/python-credit-card-validation
            # Use Luhn Algo for CC Validation

            if len(input_cc) == 16:
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
                print("The following Information is being saved: (L61)" + "\n")
                time.sleep(3)  # Sleep for 3 Seconds to imply data saved
                # Important [-4:] colon must be AFTER -4 Digits or prior digits display Ref:
                # http://codepad.org/S3zjnKoD
                print("########################################")
                print(Fore.RED + input_url, "|", input_user, "|", "XXXX XXXX XXXX", user_cc_display[-4:])
                print("url | user | Credit Card Ending")
                print(Style.RESET_ALL + "########################################")
                menu()

            else:
                time.sleep(0.2)  # Wait for 3 Seconds #https://ioflood.com/blog/python-wait/
                print(Fore.RED + "*** Error! 16 characters are required! ***")
                time.sleep(1)  # Wait for 1 Seconds
                print(Style.RESET_ALL + "-> Please Try Again")
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
                l1 = input_url  # input_url
                l2 = input_user  # input_user
                l3 = input_password  # input_password
            text_file.writelines([l0, l1, " | ", l2, " | ", l3])
            text_file.close()
            print("The following Information has been saved: L91" + "\n")
            print("########################################")
            print(Fore.RED + input_url, "|", input_user)
            print("Information Saved to file")
            print(Style.RESET_ALL + "########################################" + "\n")
            menu()

    elif menu_selection == "2":  # Open the Password.txt file.
        print("Opening passwords.txt" + "\n")  # Give a notification to the user.
        print(Fore.RED + "DOMAIN | USER | PASS | CREDIT CARD" + Style.RESET_ALL)  # Make it Red and Bloody Obvious
        view_passwords = open('passwords.txt', 'r')  # Open the file in 'r'ead mode.
        passwords = view_passwords.read()  # Show the contents of the password.txt file as "passwords"
        print(passwords + "\n")  # Print/Show the contents + new line formatting.
        menu()

    elif menu_selection == "3":  # Scare Zahir
        print(
            Fore.BLUE + "*** WARNING *** PCI-DSS Systems Daemon Activated")  # Change Colours, & Warning to show progression
        time.sleep(1)  # Sleep it, see if the user freaks out.
        print(Fore.BLUE + "*|* WARNING *|* PCI-DSS Systems Loading")
        time.sleep(1)  # Sleep it again, make it looks realistic
        print(Fore.BLUE + "*|| WARNING *|| PCI-DSS Systems Loading")
        time.sleep(1)  # Sleep once more....
        print(Fore.BLUE + "||| WARNING ||| PCI-DSS Systems Loading")
        time.sleep(0.5)
        print(Fore.YELLOW + "PCI-DSS Systems Loading: 33%.")
        time.sleep(1.5)
        print(Fore.YELLOW + "PCI-DSS Systems Loading: 66%..")
        time.sleep(1.8)
        print(Fore.LIGHTYELLOW_EX + "PCI-DSS Systems Loading: 72%..")
        time.sleep(1.8)
        print(Fore.LIGHTYELLOW_EX + "PCI-DSS Systems Loading: 99%..")
        time.sleep(2.4)
        print(Fore.RED + "PCI-DSS Systems LOADED...")
        time.sleep(1)
        print("Confirm Destroying System32 Files?")
        let_them_suffer = input("Y/N :")  # Give the User a "Choice"...
        if let_them_suffer:  # Let's give the user a dud prompt to fail at.
            print("del c:/Windows/System32/*.*")
            print("X/X")
            time.sleep(1)
            print("/X/")
            time.sleep(1)
            print("X/X")
            time.sleep(1)
            print("XXX")
            time.sleep(2)
            print("(☞ﾟヮﾟ)☞ ┬─┬")
            time.sleep(2)
            print("(╯°□°)╯︵ ┻━┻")
            time.sleep(2)
            print(text2art('''BOOM!!!
                    ''', font="small"))  # Make it fun.

            exit("Systems Offline")

        else:
            menu()
    else:
        print(text2art('''UNACCEPTABLE 
        TRY 
        AGAIN!!!
        ''', font="small"))  # Make it fun.
        menu()


menu()
