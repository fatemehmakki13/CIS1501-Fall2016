import random

num_dice = int(input('How many dice should we roll?\n'))
num_rolls = int(input('Enter number of rolls:\n'))
total_rolls = 0
totals = {  }
for number in range(num_dice,num_dice*6+1):
    totals[number] = 0

while num_rolls >= 1:
    for i in range(num_rolls):
        roll_total = 0
        for die in range(num_dice):
            roll_total += random.randint(1,6)
        
        totals[roll_total] += 1
        
        #print('Roll %d is %d (%d + %d)' % (i, roll_total, die1, die2))

    print('\nDice roll statistics:')
    for total in range(num_dice, len(totals) + num_dice):
        print( total, "was rolled", totals[total], "times")
    total_rolls += num_rolls
    num_rolls = int(input('Enter number of rolls:\n'))


print("\nDice roll histogram:")
for total in range(num_dice, len(totals) + num_dice):
    print(total,":\t",end='')
    for star in range(((int)( totals[total] / total_rolls * 100 )) ):
        print('*',end='')
    print('')
