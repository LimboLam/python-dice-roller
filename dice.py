import random
import math

dice = {1: '-----'
           '|   |'
           '| o |'
           '|   |'
           '-----', 
        2: '-----'
           '|o  |'
           '|   |'
           '|  o|'
           '-----',
        3: '-----'
           '|o  |'
           '| o |'
           '|  o|'
           '-----',
        4: '-----'
           '|o o|'
           '|   |'
           '|o o|'
           '-----',
        5: '-----'
           '|o o|'
           '| o |'
           '|o o|'
           '-----', 
        6: '-----'
           '|o o|'
           '|o o|'
           '|o o|'
           '-----'}

result = int(math.floor(random.random() * 5.99) + 1)
print(dice.get(result))