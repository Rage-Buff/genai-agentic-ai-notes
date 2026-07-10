#Rock, Paper, Scissors Game
import random

# Game settings
player_score = 0
computer_score = 0
player_money = 0
computer_money = 0
entry_fees = 10
win_amount = 20
possible_choice = ['rock', 'paper', 'scissors']

print("--- Welcome to Best of 3: Rock, Paper, Scissors! ---")

# Run until either side wins 2 rounds
while player_score < 2 and computer_score < 2:
    computer_choice = random.choice(possible_choice)
    player_choice = input('\nSelect (rock/paper/scissors): ').lower()

    if player_choice not in possible_choice:
        print('Invalid choice, round skipped.')
        continue

    print('='*30)
    print(f'Computer: {computer_choice} | You: {player_choice}')
    print('='*30)

    # Determine Winner of the Round
    if player_choice == computer_choice:
        print('Result: MATCH DRAW')
    
    elif (player_choice == 'rock' and computer_choice == 'paper') or \
         (player_choice == 'paper' and computer_choice == 'scissors') or \
         (player_choice == 'scissors' and computer_choice == 'rock'):
        print('Result: Computer wins this round! ☹️')
        computer_score += 1
        computer_money += entry_fees
        player_money -= entry_fees
    else:
        print('Result: You win this round! 😊')
        player_score += 1
        player_money += win_amount
        computer_money -= win_amount

    print(f'Score: You {player_score} - {computer_score} Computer')

# Final Results
print('\n' + '='*30)
if player_score == 2:
    print('Congratulations! You won the Best of 3!')
else:
    print('Game Over! The computer won the Best of 3.')

print(f'Final Money - You: {player_money} | Computer: {computer_money}')
