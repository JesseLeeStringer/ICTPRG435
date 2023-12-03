import time


# https://stackoverflow.com/questions/48817461/user-input-boolean-in-python
user_cc_info_answer = input('Do you need to save a Credit-Card? (Y/N) : ').lower().strip() == 'y'
if user_cc_info_answer == "Y":
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
        print("The following Information has been saved:")
        # Important [-4:] colon must be AFTER -4 Digits or prior digits display Ref:
        # http://codepad.org/S3zjnKoD
        print("URL  : ", input_url, "\n", "User: ", input_user, "\n", "XXXX XXXX XXXX",
              user_cc_display[-4:])
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
else:  # Open File & Save user Input
    text_file = open("passwords.txt", "a")
    with open('passwords.txt', 'a') as file:
        l0 = '\n'
        l1 = "domain.com"#input_url
        l2 = "user"#input_user
        l3 = "pass"#input_password
    text_file.writelines([l0, l1, " | ", l2, " | ", l3])
    text_file.close()
    print("The following Information has been saved:")
    print("URL  : ", input_url, "\n", "User: ", input_user, "\n")
    exit("Information Saved to file ")