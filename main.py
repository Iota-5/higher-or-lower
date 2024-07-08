import random


# number guessing game

def random_number_gen(low, high):
    num = random.randint(low, high)
    print(f"for testing purposes on line 8 the ans is {num}")
    return num


def check_answer(data):
    try:
        new_data = int(data)
        if new_data > answer:
            print("too much")
            return False
        elif new_data < answer:
            print("too little")
            return False
        else:
            print("correct")
            return True
    except ValueError:
        print("please insert a valid number")
        return False


def difficulty(mode):
    try:
        approved_mode = int(mode)
        if approved_mode not in [1, 2, 3]:
            return False, 1
        else:
            return True, approved_mode
    except ValueError:
        print("please insert a valid number")
        return False


num_of_guesses = 12
answer = random_number_gen(1, 100)
replay = True
system = True

while replay:
    while system:
        mode_input = input("pick a difficulty from (easy)1-3(hard) \n")
        result = difficulty(mode_input)
        if result[0]:
            game = num_of_guesses // result[1]

            while game > 0:
                user_input = input("what number am I thinking of between 1 and 100 \n")
                is_guess_correct = check_answer(user_input)
                if not is_guess_correct:
                    game -= 1
                    print(f"You have {game} attempts left.")
                else:
                    print("you win")
                    system = False
                    break
            if game <= 0:
                print("you lose")
                system = False
        else:
            print("Please enter a valid difficulty")
    user_replay = input("do you want to replay? Y/N \n")
    if not isinstance(user_replay, str):
        print("please input a valid answer")
        system = False
    else:
        formatted_replay = user_replay.lower()
        if formatted_replay == "y":
            system = True
            replay = True
            answer = random_number_gen(1, 100)
        else:
            replay = False
