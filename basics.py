import json

while True:
    print("1. Sign up")
    print("2. Sign in")
    choice = input("Enter your choice (1 or 2): ")
    if choice == '1':
        sign_up()
    elif choice == '2':
        sign_in()
        break
    else:
        print("Invalid choice. Please enter 1 or 2.")

def sign_up():
    username = input("Enter Username: ")
    password = input("Enter Password: ")
    mobile_number = input("Enter Mobile Number: ")
    user_data = load_user_data()

    if username in user_data:
        print("Username already exists. Please try a different username.")
    else:
        user_data[username] = {
            'password': password,
            'mobile_number': mobile_number
        }
        save_user_data(user_data)
        print("User signed up successfully!")

def sign_in():
    username = input("Enter Username: ")
    password = input("Enter Password: ")
    user_data = load_user_data()

    if username in user_data and user_data[username]['password'] == password:
        print(f"Welcome to the device! Your mobile number is {user_data[username]['mobile_number']}.")
    else:
        print("Incorrect credentials. Terminating the program.")

def save_user_data(data):
    with open('user_data.json', 'a') as file:
        json.dump(data, file)

def load_user_data():
    try:
        with open('user_data.json', 'r') as file:
            return json.load(file)
    except Exception as e:
        print (e)
        return {}  



