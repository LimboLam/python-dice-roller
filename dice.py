import random

dice_art = {1: 
           ('-------',
           '|     |',
           '|  o  |',
           '|     |',
           '-------'), 
        2: ('-------',
           '|o    |',
           '|     |',
           '|    o|',
           '-------'),
        3: ('-------',
           '|o    |',
           '|  o  |',
           '|    o|',
           '-------'),
        4: ('-------',
           '|o   o|',
           '|     |',
           '|o   o|',
           '-------'),
        5: ('-------',
           '|o   o|',
           '|  o  |',
           '|o   o|',
           '-------'), 
        6: ('-------',
           '|o   o|',
           '|o   o|',
           '|o   o|',
           '-------')}

dice = []
dice_amount = int(input('How many dice?: '))
total = 0

for die in range(dice_amount):
   dice.append(random.randint(1, 6))

for die in range(dice_amount):
   for line in dice_art.get(dice[die]):
      print(line)

for die in dice:
   total += die

print(total)