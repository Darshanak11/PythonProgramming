registered_emails = set()

def register_user():
    email = input("Enter your email: ")
    if email in registered_emails:
        print(f"error: {email} is already registered")
    else:
        registered_emails.add(email)
        print(f"success: {email} is now registered")

    choice = input("Do you want to register another user? (y/n): ")
    if choice == "y":
        register_user()
    else:
        print("All users registered successfully")

register_user()
