user_name=input("Enter a new user name: ")
password=input("Enter a new password: ")

print("    login   ")
a=input("Enter user name: ")
b=input("Enter password: ")

if a==user_name and b==password:
    print("login successful! Welcome!")
elif a!=user_name:
    print("User name doesn't match.Please try again.")
elif b!=password:
    print("Password doesn't match.Please try again.")
