"""
User ID: S8102226
Student: Jesse-Lee Stringer
Unit: ICTPRG435
Development Date: 03/12/2023
Source: https://github.com/JesseLeeStringer/ICTPRG435
"""
import os.path
import sys
import time
from colorama import Fore, Back, Style


def menu():
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
            print(Fore.RED + "Password Confirmed" + "\n")
            print(Style.RESET_ALL + "Commence to Credit-Card")

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
                print("The following Information is being saved: (L57)" + "\n")
                time.sleep(3)  # Sleep for 3 Seconds to imply data saved
                # Important [-4:] colon must be AFTER -4 Digits or prior digits display Ref:
                # http://codepad.org/S3zjnKoD
                print("########################################")
                print(Fore.RED + input_url, "|", input_user, "|", "XXXX XXXX XXXX", user_cc_display[-4:])
                print("url | user | Credit Card Ending")
                print(Style.RESET_ALL + "########################################")
                exit("Information Saved to file ")
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
            print("The following Information has been saved: L89" + "\n")
            print("########################################")
            print(Fore.RED + input_url, "|", input_user)
            print("Information Saved to file")
            print(Style.RESET_ALL + "########################################" + "\n")
            menu()

    elif menu_selection == "2":
        print("Opening Passwords" + "\n")
        print("domain | user | pass | Credit-Card")
        view_passwords = open('passwords.txt', 'r')
        passwords = view_passwords.read()
        print(passwords)
        print("\n")
        menu()

    elif menu_selection == "3":
        print(Fore.BLUE + "*** WARNING *** PCI-DSS Systems Daemon Activated")
        time.sleep(1)
        print(Fore.BLUE + "*|* WARNING *|* PCI-DSS Systems Loading")
        time.sleep(1)
        print(Fore.BLUE + "*|| WARNING *|| PCI-DSS Systems Loading")
        time.sleep(1)
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
        print("Confirm Destroying System32 Files? :")
        let_them_suffer = input("Y/N :")
        if let_them_suffer:
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
            time.sleep(5)
            exit("Systems Offline")
        else:
            menu()
    else:
        print("Unacceptable!" + "\n")
        menu()


menu()
