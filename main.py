import random
import time


print("\t-----WELCOME TO MENTAL MATH JUNKIE-----")
print(" The Game will evaluate your Math Reflexes 🧠 ")
print(" ")
print("---MODES---")
print("1: Amature(EASY)🤕")
print("2: Pro(MEDIUM)🔥")
print("3: Monk Mode(HARDEST)🗿")
print("ANY KEY: EXIT 🚶")

choice = int(input("Enter your Level: "))

if choice == 1:
    print(" ")
    print("You've Entered: Amature(EASY)🤕 MODE")
    print(" ")
    start_time = time.time()
    score = 0
    i = 0

    while i < 10:
        num1 = random.randint(0, 10)
        num2 = random.randint(1, 10)  # Make sure num2 is not zero for division
        operation = random.choice(['+', '-'])

        if operation == '+':
            result = num1 + num2
        elif operation == '-':
            result = num1 - num2

        answer = input(f"-> Problem {i+1}: {num1} {operation} {num2} = ")

        # Validate the user's input
        try:
            if float(answer) == result:
                print("Correct!")
                score += 1
            else:
                print(f"Wrong! The correct answer is {result}")
        except ValueError:
            print("Invalid input. Please enter a number.")

        i += 1

    end_time = time.time()
    total_time = end_time - start_time

    print("---------------------------------------")
    print(f"You scored a total of {score} points")
    if score >= 8:
        print("\t\tYOU ARE BETTER THAN AMATURE, GO TRY THE PRO MODE🔥🔥🔥")
    if score >= 5 and score < 8:
        print("\t\tTRY AGAIN NEXT TIME")
    if score < 5:
        print("\t\tYOU SURE YOU PASSED ELEMENTARY...🤣")
    print(f"You took a total of {total_time:.2f} seconds")

elif choice == 2:
    print(" ")
    print("You've Entered: Pro(MEDIUM)🔥 MODE")
    print(" ")
    start_time = time.time()
    score = 0
    i = 0

    while i < 10:
        num1 = random.randint(10, 100)
        num2 = random.randint(11, 100)  # Make sure num2 is not zero for division
        operation = random.choice(['+', '-', '*'])

        if operation == '+':
            result = num1 + num2
        elif operation == '-':
            result = num1 - num2
        elif operation == '*':
            result = num1 * num2

        answer = input(f"-> Problem {i+1}: {num1} {operation} {num2} = ")

        # Validate the user's input
        try:
            if float(answer) == result:
                print("Correct!")
                score += 1
            else:
                print(f"Wrong! The correct answer is {result}")
        except ValueError:
            print("Invalid input. Please enter a number.")

        i += 1

    end_time = time.time()
    total_time = end_time - start_time

    print("---------------------------------------")
    print(f"You scored a total of {score} points")
    if score >= 8:
        print("\t\tYOU ARE BETTER THAN PRO, GO TRY THE MONK MODE🔥🔥🔥")
    if score >= 5 and score < 8:
        print("\t\tTRY AMATURE MODE NEXT TIME")
    if score < 5:
        print("\t\tYOU ARE WORST THAN I THOUGHT😂")
    print(f"You took a total of {total_time:.2f} seconds")

elif choice == 3:
    print(" ")
    print("You've Entered: Monk Mode(HARDEST)🗿")
    print(" ")
    start_time = time.time()
    score = 0
    i = 0

    while i < 10:
        num1 = random.randint(100, 1000)
        num2 = random.randint(101, 1000)  # Make sure num2 is not zero for division
        operation = random.choice(['+', '-', '*', '/'])

        if operation == '+':
            result = num1 + num2
        elif operation == '-':
            result = num1 - num2
        elif operation == '*':
            result = num1 * num2
        elif operation == '/':
            result = num1 / num2

        answer = input(f"-> Problem {i+1}: {num1} {operation} {num2} = ")

        # Validate the user's input
        try:
            if float(answer) == result:
                print("Correct!")
                score += 1
            else:
                print(f"Wrong! The correct answer is {result}")
        except ValueError:
            print("Invalid input. Please enter a number.")

        i += 1

    end_time = time.time()
    total_time = end_time - start_time

    print("---------------------------------------")
    print(f"You scored a total of {score} points")
    if score >= 8:
        print("\t\tYOU ARE THE REAL MONK🔥🔥🔥")
    if score >= 5 and score < 8:
        print("\t\tTRY PRO MODE NEXT TIME")
    if score < 5:
        print("\t\tYOU ARE AMATURE, GO PLAY WITH TOYS")
    print(f"You took a total of {total_time:.2f} seconds")

else:
    print(" ")
    print("---PROGRAM TERMINATED---")
    exit()
