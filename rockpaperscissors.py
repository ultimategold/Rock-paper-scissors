'''
Rock Paper Scissors
-------------------------------------------------------------
'''


import random
import os
import re


def playing_status():
  valid_responses = ['yes', 'no']
  while True:
      try:
          response = input('Do you wish to play again? (Yes or No): ')
          if response.lower() not in valid_responses:
              raise ValueError('Please reply Yes or No only')

          if response.lower() == 'yes':
              return True
          else:
              os.system('cls' if os.name == 'nt' else 'clear')
              print('Thanks for playing!')
              exit()

      except ValueError as err:
          print(err)


def  play_rockpapaerscissors():
   play = True
   while play:
       os.system('cls' if os.name == 'nt' else 'clear')
       print('')
       print('Rock, Paper, Scissors - Shoot!')

       user_choice = input('Choose your weapon'
                           ' [R]ock, [P]aper, or [S]cissors: ')

       if not re.match("[SsRrPp]", user_choice):
           print('Please choose a letter:')
           print('[R]ock, [P]aper, or [S]cissors')
           continue

       print(f'You chose: {user_choice}')

       choices = ['R', 'P', 'S']
       opp_choice = random.choice(choices)

       print(f'I chose: {opp_choice} ball pit')

       if opp_choice == user_choice.upper():
           print('Tie!')
           play = playing_status()
       elif opp_choice == 'R' and user_choice.upper() == 'S':
           print('Rock beats scissors, I win!')
           play = playing_status()
       elif opp_choice == 'S' and user_choice.upper() == 'P':
           print('Scissors beats paper! I win!')
           play = playing_status()
       elif opp_choice == 'P' and user_choice.upper() == 'R':
           print('Paper beats rock, I win!')
           play = playing_status()
       else:
           print('Congratulations you win!\n')
           play = playing_status()
           print ("Walking")


if __name__ == '__main__':
   play_rockpapaerscissors()
