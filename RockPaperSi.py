"""
1 - Rock
2 - Paper
3 - Scissors

Rock eats Scissors
Paper eat Rock
Scissors eats Paper
"""

import random
import time

li: list = [1, 2, 3]
# Scores of user and computer
user_score = 0
com_score = 0

keypair: dict = {
    1: 'Rock',
    2: 'Paper',
    3: 'Scissors'
}


# Method to print Scores of user and computer
def print_score(a, b):
    print(f"""
    --------------------------------
    | User Score | Computer Score  |
    --------------------------------
    |      {a}     |        {b}        |
    --------------------------------
""")


if __name__ == "__main__":
    while True:
        # Asking user to enter to play the game or not
        choice: str = input("Y/y to continue N/n to quit:").lower()
        if choice == "n":

            print("Bye see you later....")
            time.sleep(1.5)
            break
        elif choice == 'y':
            # Taking user input until he entered correct
            while True:
                user_input: str = input("""
                Enter
                1 - Rock
                2 - Paper
                3 - Scissors 
                """)
                try:
                    int_num = int(user_input)
                    if int_num in range(1, 4):
                        break
                    else:
                        print("Enter input again")
                except ValueError:
                    print("The string is not a valid number.")

            print(f"User :- {keypair[int_num]}")

            # Computer chose a random input from the above list
            com_input: int = random.choice(li)
            print("computer choice.....")
            time.sleep(1)

            print(f"Computer :- {keypair[com_input]}")

            if int_num == com_input:
                print("draw")
            elif int_num == 1:
                if com_input == 2:
                    print("Computer won")
                    com_score += 1
                else:
                    print("User Won")
                    user_score += 1
            elif int_num == 2:
                if com_input == 1:
                    print("User won")
                    user_score += 1
                else:
                    print("computer won")
                    com_score += 1

            else:
                if com_input == 2:
                    print("user won")
                    user_score += 1
                else:
                    print("computer won")
                    com_score += 1
            print_score(user_score, com_score)

        else:
            print("Chosen Wrong choice, Enter again")
