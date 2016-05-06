from random import randint
import time

#Asking the user to input the number of prisoners
number_of_prisoners = input('With how many prisoners do you want to play the game? ')

prison = []

#Function to fill the prison with the user given number of prisoners as str.
def get_list_of_prisoners(number,list_to_fill):
  for i in range (1,number + 1):
    list_to_fill.append(str(i))
  return list_to_fill

prisoners = get_list_of_prisoners(number_of_prisoners,prison)

print 'Here are your prisoners locked up one by one :'
print prisoners

#Setting the variables
lamp = 0
been_there = []
ticks_made_by_counter = 0
rounds = 0

##Chose the counter who goes out first and turns off the lamp if it is on.
def who_will_count(prisoners):
  random_index = randint(0,len(prisoners)-1)
  prisoners[random_index] = 'counter'
  return prisoners

prisoners = who_will_count(prisoners)

time.sleep(4)
print 'START'
time.sleep(1)

##Start to count
while ticks_made_by_counter < len(prisoners)-1:
  rounds += 1
  choosen_one = prisoners[randint(0,len(prisoners)-1)]
  print 'Round : %s --- The prisoner who goes outside this round is : %s' % (rounds,choosen_one)
  #time.sleep(0.2)
  if choosen_one == 'counter' and lamp == 1:
    ticks_made_by_counter += 1
  elif choosen_one != 'counter' and choosen_one not in been_there and lamp == 0:
    lamp = 1
    been_there.append(choosen_one)
print 'FINISH'
time.sleep(1)
print 'It took %s rounds to reach full accuracy.' % (rounds)
print 'I as a counter turned off the lamp %s times' % (ticks_made_by_counter)
print 'By now all the %s prisoners including me were already outside.' % (len(prisoners))  








