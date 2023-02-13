#define variables from user input

gain = int(input('How much LP do you gain?\n'))
lose = int(input('\nHow much LP do you lose?\n'))
goal = int(input('\nHow much LP do you need to gain?\n'))

#define formulas

def lol_calc_variables(wins, losses):
    total_lp_gained = gain * wins
    total_lp_lost = lose * losses
    rate = total_lp_gained - total_lp_lost
    gain_over_rate = (goal / rate)
    answer = round(gain_over_rate * 20) + 5 #add 5 for promos
    return answer

#define the calc function

def lol_calculator(gain, lose, goal):

    print("\n")

    #check 55% win rate
    answer = lol_calc_variables(11, 9)   

    if answer > 0:
        print("You will need to play at least {0:.0f} games with a >=55% win rate to reach your goal\n".format(answer))
    else:
        print("55% win rate is not enough\n")


    #check 60% win rate    
    answer = lol_calc_variables(12, 8)    

    if answer > 0:
        print("You will need to play at least {0:.0f} games with a >=60% win rate to reach your goal\n".format(answer))
    else:
        print("60% win rate is not enough\n")

    
    #check 65% win rate
    answer = lol_calc_variables(13, 7)
    
    if answer > 0:
        print("You will need to play at least {0:.0f} games with a >=65% win rate to reach your goal\n".format(answer))
    else:
        print("65% win rate is not enough\n")

    
    #check 70% win rate
    answer = lol_calc_variables(14, 6)    

    if answer > 0:
        print("You will need to play at least {0:.0f} games with a >=70% win rate to reach your goal\n".format(answer))
    else:
        print("You need to raise your MMR or maintain a >70% win rate every 20 games\n")

lol_calculator(gain, lose, goal)