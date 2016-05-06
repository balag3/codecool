

import random

def roll():
    return random.randint(1,6)

def player_move(numRolls):
    solution = []
    for i in range(numRolls):
        solution.append(roll())
    return solution

def pretty_print(player,aList):
    if len(aList) == 3:
      print (player,aList[0],'-',aList[1],'-',aList[2])
      return ''
    elif len(aList) == 2:
        print (player,aList[0],'-',aList[1])
        return ''
    elif len(aList) == 1:
        print (player,aList[0])
        return ''

def calculate_outcome(attacker_rolls,defender_rolls,defender_count):
    attacker_loss = 0
    defender_loss = 0
    outcome = [0,0]
    for i in range(int(defender_count)):
        max_a = max(attacker_rolls)
        max_d = max(defender_rolls)
        if max_a > max_d:
            defender_loss += 1
            attacker_rolls[attacker_rolls.index(max_a)] = 0
            defender_rolls[defender_rolls.index(max_d)] = 0
            # attacker_rolls.pop(attacker_rolls.index(max_a))
            # defender_rolls.pop(defender_rolls.index(max_d))
        elif max_d >= max_a:
            attacker_loss += 1
            attacker_rolls[attacker_rolls.index(max_a)] = 0
            defender_rolls[defender_rolls.index(max_d)] = 0
            # attacker_rolls.pop(attacker_rolls.index(max_a))
            # defender_rolls.pop(defender_rolls.index(max_d))
    outcome[0] = attacker_loss
    outcome[1] = defender_loss
    return outcome


def ask_input(question,possible_rolls):
    answer = input(question)
    if answer not in possible_rolls:
        return ask_input(question,possible_rolls)
    return int(answer)







attacker_question = 'How many units attack? '
defender_question = 'How many units defend? '

attacker_possible_rolls = ['1','2','3']
defender_possible_rolls = ['1','2']

attacker = 'Attacker:'
defender = 'Defender:'

attacker_count = ask_input(attacker_question,attacker_possible_rolls)
defender_count = ask_input(defender_question,defender_possible_rolls)

attack_roll = player_move(attacker_count)
defend_roll = player_move(defender_count)

print('')
print ('Dice:')
print (pretty_print(attacker,attack_roll))
print (pretty_print(defender,defend_roll))


final = calculate_outcome(attack_roll,defend_roll,defender_count)


print ('Outcome: ')
print (attacker, " Lost %s unit" % (final[0]))
print('')
print (defender, " Lost %s unit" % (final[1]))
