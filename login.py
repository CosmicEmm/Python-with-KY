import time

username = "lugia"
password = "secretpassword"

username_input = input("Username: ")
password_input = input("Password: ")

if username_input == username and password_input == password:
    print("Access Granted")
    print("Please wait while we pull up the secret mainframe... ")
    time.sleep(5)
    print("Checking for Security Key...")
    time.sleep(2)
    print("Security Key verified")
    time.sleep(1)
    print("Activating DeepMind...")
    time.sleep(2)
    print("DeepMind activated. Decrypting national security secrets...")
elif username_input == username and password_input != password:
    print("Password Incorrect")
elif username_input != username and password_input == password:
    print("Username Incorrect")
else:
    print("Both username and password are incorrect. Try again!")


