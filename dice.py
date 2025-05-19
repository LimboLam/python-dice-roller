import random

dice = {1, 2, 3, 4, 5, 6}
dice_amount = int(input('How many dice do you want?: '))

def roll_dice():
    result = int(round(random.random() * 5))