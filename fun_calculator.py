
import random

print("===== FUN CALCULATOR =====")

while True:
    print("\n1. Calculator")
    print("2. Generate Lucky Number")
    print("3. Random Activity")
    print("4. Number Guessing Game")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            print("Choose an operation: +, -, *, /")
            operator = input("Enter operator: ")

            if operator == "+":
                print("Result:", num1 + num2)
            elif operator == "-":
                print("Result:", num1 - num2)
            elif operator == "*":
                print("Result:", num1 * num2)
            elif operator == "/":
                if num2 != 0:
                    print("Result:", num1 / num2)
                else:
                    print("Error! Cannot divide by zero.")
            else:
                print("Invalid operator!")

        except ValueError:
            print("Please enter valid numbers!")

    elif choice == "2":
        lucky_number = random.randint(1, 100)
        print("Your lucky number is:", lucky_number)
        print("Have a lucky day!")

    elif choice == "3":
        activities = [
            "Read a book",
            "Draw a picture",
            "Play a game",
            "Listen to music",
            "Learn something new",
            "Do a fun science experiment"
        ]

        activity = random.choice(activities)
        print("Your random activity is:", activity)

    elif choice == "4":
        secret_number = random.randint(1, 20)
        attempts = 0

        print("Guess the number between 1 and 20!")

        while True:
            try:
                guess = int(input("Enter your guess: "))

                if guess < 1 or guess > 20:
                    print("Enter a number between 1 and 20.")
                    continue

                attempts += 1

                if guess < secret_number:
                    print("Too low! Try a bigger number.")
                elif guess > secret_number:
                    print("Too high! Try a smaller number.")
                else:
                    print("Congratulations! You guessed it!")
                    print("Number of attempts:", attempts)
                    break

            except ValueError:
                print("Please enter a whole number!")

    elif choice == "5":
        print("Thanks for using the Fun Calculator!")
        break

    else:
        print("Invalid choice! Please enter 1, 2, 3, 4, or 5.")
