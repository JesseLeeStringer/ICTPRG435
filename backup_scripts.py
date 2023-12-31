import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog


def openfile():
    filename = filedialog.askopenfilename(initialdir="/",
                                          title="Open File",
                                          filetypes=(("Text Files", "*.txt"), ("All Files", "*.*")))
    try:
        if filename:
            the_file = open(filename)
            textArea.insert(tk.END, the_file.read())
            the_file.close()
        elif filename == '':
            messagebox.showinfo("Cancel", "You clicked Cancel")
    except IOError:
        messagebox.showinfo("Error", "Could not open file")


form = tk.Tk()
form.title("Passwords")

'''
def user_menu_selection():
    print("1. Input Credentials")
    print("2. View Passwords")
    print("3. View Credit-Card")
    print("4. Exit")
    user_menu_selection = input("Please select: ")

user_menu_selection()
if (user_menu_selection == "1"):
    # Print user input, take entries, define as strings
    print("Please enter your credentials")
    input_url = input("url: ")
    print(input_url)

    input_user = input("user: ")
    print("Confirming:", input_url, " | ", input_user)

    input_password = input("password: ")
    input_password_confirm = input("confirm password: ")
    if input_password != input_password_confirm:
        exit("Passwords do not match")
    else:
        input_cc_question = input("Do you need to save a Credit-Card? (Y/N) :")
        # need to work out boolean logic on this,
        # user_cc_input_question = input_cc_question.lower() in ["y", "yes"]
        # user_cc_input_question == "y":

        print("Credit-Card Numbers MUST be 16 characters")
        input_cc = input("Credit Card Number: ")

        if len(input_cc) == 16:
            print("Credit-Card ending in", input_cc[-4:], "Saved Successfully")
            user_cc_display = input_cc
            # Open File & Save user Input
            text_file = open("passwords.txt", "a")
            with open('passwords.txt', 'a') as file:
                l0 = '\n'
                l1 = input_url
                l2 = input_user
                l3 = input_password
                l4 = input_cc
            text_file.writelines([l0, l1, " | ", l2, " | ", l3, " | ", l4])
            text_file.close()
            print("The following Information has been saved:")
            # Important [-4:] colon must be AFTER -4 Digits or prior digits display Ref: http://codepad.org/S3zjnKoD
            print("URL  : ", input_url, "\n", "User: ", input_user, "\n", "XXXX XXXX XXXX", user_cc_display[-4:])
            exit("Information Saved to file ")

        else:
            time.sleep(0.2)  # Wait for 3 Seconds #https://ioflood.com/blog/python-wait/
            print("*** Error! 16 characters are required! ***")
            time.sleep(3)  # Wait for 3 Seconds
            print("-> Returning to Menu")
            time.sleep(3)  # Wait for 3 Seconds
            print("...")
            print(" ..")
            print("  .")


elif user_menu_selection == "2":
    print("Opening Password")


elif user_menu_selection == "3":
    print("Selection #3")
else:
    user_menu_selection == "4"
    print("Selection #4")
'''
