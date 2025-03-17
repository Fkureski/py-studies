login = input("Username:")
login_password = input("Password:")

username = "admin"
password = "1234"

if (login == username and login_password == password):
    print("Logged in")
else:
    print("Username or password is incorrect")