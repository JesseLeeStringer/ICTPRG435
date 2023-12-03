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

# # https://stackoverflow.com/questions/40688156/python-credit-card-validation
''' def check_second_digits(num):
                length = len(num)
                sum = 0
                for i in range(length - 2, -1, -2):
                    number = eval(num[i])
                    number = number * 2
                    if number > 9:
                        strnumber = str(number)
                        number = eval(strnumber[0]) + eval(strnumber[1])
                        sum += number
                    return sum

            def odd_digits(num):
                length = len(num)
                sumodd = 0
                for i in range(length - 1, -1, -2):
                    num += eval(num[i])
                return sumodd

            def c_length(num):
                length = len(num)
                if num >= 13 and num <= 16:
                    if num[0] == "4" or num[0] == "5" or num[0] == "6" or (num[0] == "3" and num[1] == "7"):
                        return True
                    else:
                        return False

            def cc_algo():
                cc = (input_cc.readline().strip())
                print(format("Card Number", "20s"), ("Valid / Invalid"))
                print("------------------------------------")
                while cc != "EXIT":
                    even = check_second_digits(num)
                    odd = odd_digits(num)
                    c_len = c_length(num)
                    tot = even + odd

                    if c_len == True and tot % 10 == 0:
                        print(format(cc, "20s"), format("Valid", "20s"))
                    else:
                        print(format(cc, "20s"), format("Invalid", "20s"))
                    num = (input_cc.readline().strip())
'''