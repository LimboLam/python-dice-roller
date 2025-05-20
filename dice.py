import random
import math

dice = {1: '-------\n'
           '|     |\n'
           '|  o  |\n'
           '|     |\n'
           '-------', 
        2: '-------\n'
           '|o    |\n'
           '|     |\n'
           '|    o|\n'
           '-------',
        3: '-------\n'
           '|o    |\n'
           '|  o  |\n'
           '|    o|\n'
           '-------',
        4: '-------\n'
           '|o   o|\n'
           '|     |\n'
           '|o   o|\n'
           '-------',
        5: '-------\n'
           '|o   o|\n'
           '|  o  |\n'
           '|o   o|\n'
           '-------', 
        6: '-------\n'
           '|o   o|\n'
           '|o   o|\n'
           '|o   o|\n'
           '-------'}

result = int(math.floor(random.random() * 5.99) + 1)
print(dice.get(result))