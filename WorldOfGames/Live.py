from GuessGame import play as GuessGamePlay
from MemoryGame import play as MemoryGamePlay
from CurrencyRouletteGame import play as CurrencyRouletteGamePlay
from Score import add_score

def welcome(name):
    print(f"Hello {name} and welcome to the World of Games (WoG).")
    print("Here we can find many cool games to play.")

def load_game():
    print("Please choose a game to play:")
    print("1. Memory Game -  a sequence of numbers will appear 1 second and you have to guess it back")
    print("2. Guess Game - guess the number and see if you chose like the computer")
    print("3. Currency Roulette - try and guess the value of a random amount of USD in ILS")
    GetResult = 0
    GetDiff = 0
    try:
        GetResult = int(input("Which game would you like to play? "))
        while (int(GetResult) is None or not 1 <= GetResult <= 3):
            print("The game you choose is wrong please choose again")
            GetResult = int(input("Which game would you like to play? "))
    except ValueError:
        load_game()
        return
    try:
        GetDiff = int(input("Please choose game difficulty from 1 to 5: "))
        while (int(GetDiff) is None or not 1 <= GetDiff <= 5):
            print("The difficulty you choose is wrong please choose again")
            GetDiff = int(input("Please choose game difficulty from 1 to 5: "))
    except ValueError:
        load_game()
        return
    result = False
    if (GetResult == 1):
        result = MemoryGamePlay(GetDiff)
    elif (GetResult == 2):
        result = GuessGamePlay(GetDiff)
    elif (GetResult == 3):
        result = CurrencyRouletteGamePlay(GetDiff)

    if (result):
        add_score(GetDiff)
        print("you won!")
    else:
        print("you lost :/")

