import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("Welcome to the Password Generator!")
    
    # Request user input for password length
    try:
        length = int(input("Enter the preferred password length: "))
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        return
    
    # Generate and display the password
    if length <= 0:
        print("Password length must be greater than 0.")
    else:
        password = generate_password(length)
        print("Generated Password: ", password)

if __name__ == "__main__":
    main()
