username = "ItsDenji777"
password = "10891089"

user_input = input("Enter your Userame: ")
pass_input = input("Enter your Password: ")

if user_input == username and pass_input == password:
    print(f"Welcome Back {username}!")
else:
    print("Incorrect username or password. Please try again.")