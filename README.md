# 3x3 Slot Machine Simulator 🎰

## Overview
This project is a simulation of a **3x3 slot machine** game with a single payline (the middle row). The game includes **5 symbols**, including a special **Jackpot** symbol i.e. `[1,2,3,4,7]`. Players can spin the reels, bet a fixed amount per spin, and win based on symbol combinations in the middle row. The game also calculates the **Return to Player (RTP)** after each set of spins.


## Features
- **Symbols & Paylines**: 5 distinct symbols with different payout values, including a special **Jackpot** symbol.
- **Randomized Reels**: Each reel is populated with symbols based on a predefined frequency distribution.
- **Winning Conditions**:
  - A win occurs when the three symbols in the middle row match.
  - A **Jackpot win** triggers a grand payout.
  - Regular wins are based on symbol-specific payouts.
- **User-Defined Spins**: Players can choose the number of spins.
- **Return to Player (RTP)**: Calculates and displays RTP after all spins.
- **Balance Management**: The player's balance updates after each spin based on wins and spin costs.

## Requirements
- Python 3.x

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/kanish-h-h/slot-machine-simulator.git
   ```

2. Navigate to the project directory:
```bash
cd slot-machine-simulator
```

## How to Play
1. Run the game:
```python
python3 main.py
```
2. Enter your betting amount (minimum $10).
3. Enter the number of spins.
4. Press ENTER to spin the reels.

The game will display:
- The symbols for each spin.
- The total payout for each spin.
- The player's current balance after each spin.

At the end, the game shows:
- Total spins.
- Total wins.
- Total **Jackpot** wins.
- Total bet amount.
- Total winnings.
- **RTP** percentage.

## Example Output
```python
Enter your betting amount (minimum $10): $10
Enter the number of spins: 5

Press ENTER to spin....
   ['1', '1', '4']
-> ['4', '1', '2'] <-
   ['4', '2', '2']
Total payout for this spin: 0
Player's current balance: $8.00

...............
...............
...............

Press ENTER to spin....
   ['1', '1', '4']
-> ['1', '7', '4'] <-
   ['3', '3', '3']
Total payout for this spin: 0
Player's current balance: $6.00

--- Game Over ---
Total spins: 5
Total wins: 2
Total Jackpot wins: 0
Total Bet: $10.00
Total Winnings: $12.50
RTP: 125.00%

```

## Project Structure

```bash
.
├── config.py            # Contains the symbols, payout structure, and frequency table
├── main.py              # Entry point of the game
├── game.py              # Handles the game logic
├── slot_machine.py      # Contains the SlotMachine class
└── README.md            # Project documentation
```

## Symbols & Payouts

|Symbol|Payout for 3 Symbols|Payout for 2 Symbols|Payout for 1 Symbol|
|---|---|---|---|
|1|5|1|0.5|
|2|10|2|1|
|3|20|5|2|
|4|40|10|5|
|7 (Jackpot)|1000|N/A|N/A|


## RTP Calculation
The **Return to Player (RTP)** is calculated as:
```mathematica
RTP = (Total Winnings / Total Bet) * 100
```


