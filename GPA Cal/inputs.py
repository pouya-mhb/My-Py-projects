from typing import List


def prompt_scores() -> list:
    scores = []
    counter = 1
    while True:
        try:
            print(f"Enter values for grade and unit for course no. {counter}.")
            grade = float(input("Grade: "))
            unit = int(input("Unit: "))
            scores.append((grade, unit))
            counter = counter + 1
        except:
            print("Wrong input. Trying again...")
            continue
        user_command = input("Add another? (Y/n)")
        if user_command.lower() == 'n':
            break

    return scores
