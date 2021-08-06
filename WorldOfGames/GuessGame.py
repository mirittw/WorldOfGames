import random

def generate_number(diffeculty):
    ComputerNumber = random.randint(1, diffeculty)
    return ComputerNumber

def get_guess_from_user(diffeculty):
    try:
        GetResult = int(input(f"choose a number between 1 - {diffeculty} "))
        while (int(GetResult) is None or not 1 <= GetResult <= diffeculty):
            GetResult = int(input("you didnt chose in range, please try again "))
        return GetResult
    except ValueError:
        return 0

def compare_results(computer, user):
    if computer == user:
        return True
    else:
        return False

def play(diffeculty):
    comp = generate_number(diffeculty)
    user = get_guess_from_user(diffeculty)
    while (user == 0):
        user = get_guess_from_user(diffeculty)
    return(compare_results(comp, user))