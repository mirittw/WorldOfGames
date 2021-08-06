import random
import time
from Utils import Screen_cleaner

def generate_sequence(diffeculty):
    ComputerNumber = []
    for i in range(diffeculty):
        ComputerNumber.append(random.randint(1, 101))
    return ComputerNumber

def get_list_from_user(diffeculty):
    try:
        GetResult = []
        for i in range(diffeculty):
            GetResult.append(int(input(f"choose a number in the location - {i + 1} ")))
        return GetResult
    except ValueError:
        return 0

def is_list_equal(computer, user, diffeculty):
    for i in range(diffeculty):
        if computer != user:
            return False
    return True

def play(diffeculty):
    comp = generate_sequence(diffeculty)
    print(comp)
    time.sleep(0.7)
    print("\r\n" * 100)
    Screen_cleaner()
    user = get_list_from_user(diffeculty)
    while (user == 0):
        user = get_list_from_user(diffeculty)
    return(is_list_equal(comp, user, diffeculty))