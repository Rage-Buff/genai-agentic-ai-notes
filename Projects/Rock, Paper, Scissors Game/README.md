# Rock, Paper, Scissors (Best of 3)

A simple Python command-line implementation of the classic **Rock, Paper, Scissors** game where you play against the computer in a **Best of 3** match.

## Features

* Best of 3 gameplay (first to 2 wins).
* Random computer moves.
* Input validation for invalid choices.
* Round-by-round score updates.
* Simple money tracking system.
* Final winner announcement.

## How to Run

1. Make sure Python 3 is installed.
2. Save the file as `rock_paper_scissors.py`.
3. Run the program:

   ```bash
   python rock_paper_scissors.py
   ```

## How to Play

* Enter one of the following:

  * `rock`
  * `paper`
  * `scissors`
* Invalid inputs are ignored, and you'll be asked again.

## Game Rules

* Rock beats Scissors.
* Scissors beats Paper.
* Paper beats Rock.
* First player to win **2 rounds** wins the match.

## Money System

* Losing a round costs **10** coins.
* Winning a round earns **20** coins.
* Your final balance is displayed at the end of the game.

## Technologies Used

* Python 3
* `random` module

