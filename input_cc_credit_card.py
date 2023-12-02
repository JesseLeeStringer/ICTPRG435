import time

print("Credit-Card Numbers MUST be 16 characters")
input_cc = input("credit card: ")

# Copy input_cc into a new string to save to input_cc into textfile, and show truncated string value

# https://stackoverflow.com/questions/8761778/limiting-python-input-strings-to-certain-characters-and-lengths
if len(input_cc) == 16:
    print("Credit-Card ending in", user_cc_display[-4:], "Saved Successfully")
else:
    time.sleep(0.2) # Wait for 3 Seconds #https://ioflood.com/blog/python-wait/
    print("*** Error! 16 characters are required! ***")
    time.sleep(3) # Wait for 3 Seconds
    print("-> Returning to Menu")
    time.sleep(3)  # Wait for 3 Seconds
    print("...")
    print(" ..")
    print("  .")
