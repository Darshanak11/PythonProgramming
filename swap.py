def main():
    try:
        a = float(input("Enter the first number: "))
        b = float(input("Enter the second number: "))
    except ValueError:
        print("Invalid input. Please enter valid numbers.")
        return

    print(f"Before swapping: a = {a}, b = {b}")
    # Swapping the two numbers
    a, b = b, a
    print(f"After swapping: a = {a}, b = {b}")

if __name__ == "__main__":
    main()