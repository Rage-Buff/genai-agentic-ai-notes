#Random Number Guessing Game
import random
print('Welcome to Random Number Guessing Game')
comp= random.randint(1,10)
try:
  user= int(input('Guess a number: '))
except:
  print('Invalid input')
else:
  if comp == user:
    print('😁You Won😁')
    print('My number was also',comp)
  else:
     print('🤦‍♂️You Lose🤦‍♂️')
     print('The number was' ,comp)
