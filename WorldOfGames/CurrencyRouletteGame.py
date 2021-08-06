import random
from currency_converter import CurrencyConverter

def get_money_interval(diffeculty, rand):
    c = CurrencyConverter()
    t = int(c.convert(rand, 'USD', 'ILS'))
    return (t - (5 - diffeculty), t + (5 - diffeculty))

def get_guess_from_user(rand):
    try:
        GetResult = int(input(f"guess the value for {rand} USD to ILS "))
        return GetResult
    except ValueError:
        return -1

def play(diffeculty):
    rand = random.randint(1, 100)
    comp = get_money_interval(diffeculty, rand)
    user = get_guess_from_user(rand)
    while (user == -1):
        user = get_guess_from_user(diffeculty)
    return(comp[0] <= user <= comp[1])